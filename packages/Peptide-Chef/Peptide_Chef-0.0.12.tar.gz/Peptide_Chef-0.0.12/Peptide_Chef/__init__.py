### Data Handling
import numpy as np
import pandas as pd
from pandas import ExcelWriter
import openpyxl
import re
import itertools as it
from collections import deque
from pyteomics import fasta, parser, electrochem, mass
from itertools import combinations
from urllib.request import urlretrieve
import gzip
from functools import lru_cache

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# File Handling Functions

@lru_cache(maxsize=None)
def CookBook(Species=None,homebrew=False, takeout=True,url=None,measure=False,target=None):
    #Use to import fasta.gz files directly from uniprot (Takeout) with a provided url (Default is Human) or from local folder using homebrew hyperparameter.
    # Takeout is default, Takeout must be switched to False for Homebrew to be True.
    # accepts Uniprot format
    ingredients=list()
    if url == None:
        url="https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640/UP000005640_9606.fasta.gz"
    if (homebrew == True) & (takeout==True):
        print("Only one method (homebrew/takeout) can == True...")
        print ("Takeout will be automatically selected...")
    if takeout is True:
        homebrew=False
        print('Downloading the FASTA file from url...')
        urlretrieve(url,'temp.fasta.gz')
        print('Unzipping...')
        with gzip.open('temp.fasta.gz', mode='rt') as gzfile:
            for info, contents in fasta.FASTA(gzfile):
                taste=list((info,contents))
                ingredients.append(taste)
                recipie=pd.DataFrame(ingredients,columns=['ID','Peptide'])
        print("Takeout is Done!")
    if homebrew is True:
        if Species == None:
            print("Provide Species identification. This will be the name of the local FASTA file.")
        print("Downloading the FASTA file from local flle...")
        book = str(Species+".fasta")
        recipie=pd.DataFrame()
        print("Serving up a homebrew...")
        with fasta.read(book) as menu:
            for info, contents in menu:
                taste=list((info,contents))
                ingredients.append(taste)
                recipie=pd.DataFrame(ingredients,columns=['ID','Peptide'])
        print("Homebrow is Done!")
    recipie[['db', 'UniprotID','ID2']] = recipie['ID'].str.split('|', 2, expand=True)
    recipie[['Gene','Identification']] = recipie['ID2'].str.split('_', 1, expand=True)
    recipie.drop(columns=['ID', 'ID2',"db"], inplace=True)
    if measure == True:
        recipie["Protein_Length"]=recipie[target].str.len()
    print("Here ya go boss!")
    return(recipie)

def MeatWrapper(workbook,old,new,output):
    meat = openpyxl.load_workbook(workbook)
    wrap = meat[old]
    wrap.title = new
    meat.save(output)

def Excel_Mapper(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()

def PEAKS_Importer(csv,drop_OG=True):
    df=pd.read_csv(csv)
    df[["Protein","Y"]]=df['Protein Accession'].str.split("|",1,expand=True)
    df[["Gene","Species"]]=df['Y'].str.split("_",1,expand=True)
    if drop_OG==True:
        df.drop(columns=['Y', 'Protein Accession',"Found By"], inplace=True)
    else:
        df.drop(columns=['Y',"Found By"], inplace=True)
    return(df)

def Peptide_Origin(origin,target,Origin_Key=None,Target_Key=None,Origin_Label=None, Target_Label=None):
    # primarily used to transfer whole protein measurments (i.e. aa_length) to data_frame with peptide products. Origin_Key is
    # is used to find 'Merge' points (Target_Key) regardless of frequency (likely multiple peptides for one key/protein).Label is used
    # capture information (peptide lenght, sequence, etc) from origin to target. New_Label is optional, default uses origin label to
    # label newly created target column. 
    labeler=origin.set_index(Origin_Key).to_dict()[Origin_Label]
    if Target_Label == None:
        target[Origin_Label] = target[Target_Key].map(labeler)
    else:
        target[Target_Label] = target[Target_Key].map(labeler)
    return target

@lru_cache(maxsize=500)
def Pep2Pro(protein,peptides):
    protein = re.sub(r'[^A-Z]', '', protein)
    mask = np.zeros(len(protein), dtype=np.int8)
    for peptide in peptides:
        indices = [m.start() for m in re.finditer(
            '(?={})'.format(re.sub(r'[^A-Z]', '', peptide)), protein)]
        for i in indices:
            mask[i:i + len(peptide)] = 1
    return mask.sum(dtype=float) / mask.size


#------------------------------------------------------------------------------
# Digestion and Peptide Handling

rules = {
    'arg-c':         r'R',
    'asp-n':         r'\w(?=D)',
    'bnps-skatole' : r'W',
    'caspase 1':     r'(?<=[FWYL]\w[HAT])D(?=[^PEDQKR])',
    'caspase 2':     r'(?<=DVA)D(?=[^PEDQKR])',
    'caspase 3':     r'(?<=DMQ)D(?=[^PEDQKR])',
    'caspase 4':     r'(?<=LEV)D(?=[^PEDQKR])',
    'caspase 5':     r'(?<=[LW]EH)D',
    'caspase 6':     r'(?<=VE[HI])D(?=[^PEDQKR])',
    'caspase 7':     r'(?<=DEV)D(?=[^PEDQKR])',
    'caspase 8':     r'(?<=[IL]ET)D(?=[^PEDQKR])',
    'caspase 9':     r'(?<=LEH)D',
    'caspase 10':    r'(?<=IEA)D',
    'chymotrypsin high specificity' : r'([FY](?=[^P]))|(W(?=[^MP]))',
    'chymotrypsin low specificity':
        r'([FLY](?=[^P]))|(W(?=[^MP]))|(M(?=[^PY]))|(H(?=[^DMPW]))',
    'clostripain':   r'R',
    'cnbr':          r'M',
    'enterokinase':  r'(?<=[DE]{3})K',
    'factor xa':     r'(?<=[AFGILTVM][DE]G)R',
    'formic acid':   r'D',
    'glutamyl endopeptidase': r'E',
    'granzyme b':    r'(?<=IEP)D',
    'hydroxylamine': r'N(?=G)',
    'iodosobenzoic acid': r'W',
    'lysc':          r'K',
    'ntcb':          r'\w(?=C)',
    'pepsin ph1.3':  r'((?<=[^HKR][^P])[^R](?=[FL][^P]))|'
                     r'((?<=[^HKR][^P])[FL](?=\w[^P]))',
    'pepsin ph2.0':  r'((?<=[^HKR][^P])[^R](?=[FLWY][^P]))|'
                     r'((?<=[^HKR][^P])[FLWY](?=\w[^P]))',
    'proline endopeptidase': r'(?<=[HKR])P(?=[^P])',
    'proteinase k':  r'[AEFILTVWY]',
    'staphylococcal peptidase i': r'(?<=[^E])E',
    'thermolysin':   r'[^DE](?=[AFILMV])',
    'thrombin':      r'((?<=G)R(?=G))|'
                     r'((?<=[AFGILTVM][AFGILTVWA]P)R(?=[^DE][^DE]))',
    'trypsin':       r'([KR](?=[^P]))|((?<=W)K(?=P))|((?<=M)R(?=P))',
    'trypsin_exception': r'((?<=[CD])K(?=D))|((?<=C)K(?=[HY]))|((?<=C)R(?=K))|((?<=R)R(?=[HR]))',
}

def update_rules(new_enzyme,new_rule,rules=rules):
    dictionary.update(new_enzyme=new_rule)
    return rules

@lru_cache(maxsize=None)
def Cleaver(sequence, rule, missed_cleavages=0, min_length=None, max_length=None, exception=None):
    peptides = []
    if rule in rules:
        rule = rules[rule]
    exception = rules.get(exception, exception)
    ml = missed_cleavages + 2
    trange = range(ml) #returns range of 0 to ml-1
    cleavage_sites = deque([0], maxlen=ml) # returns positions of cleavage sites between each other. 
    if min_length is None:
        min_length = 1
    cl = 1
    if exception is not None: #locates postion of c-terminal by-product of cleavage. 
        exceptions = {x.end() for x in re.finditer(exception, sequence)}
    for i in it.chain([x.end() for x in re.finditer(rule, sequence)],
                   [None]):
        if exception is not None and i in exceptions:
            continue
        cleavage_sites.append(i)
#         print(cleavage_sites)
        if cl < ml:
            cl += 1
        for j in trange[:cl - 1]:
            seq = sequence[cleavage_sites[j]:cleavage_sites[-1]]
            if (len(seq) >= min_length):
                if (len(seq) <= max_length):
                    peptides.append(seq)
    return peptides

class Scales:
    def Mass(peptide):
        mass = {  
        "A": 71.037114,
        "R": 156.101111,
        "N": 114.042927,
        "D": 115.026943,
        "C": 103.009185,
        "Q": 129.042593,
        "E": 128.058578,
        "G": 57.021464,
        "H": 137.058912,
        "I": 113.084064,
        "L": 113.084064,
        "K": 128.094963,
        "M": 131.040485,
        "F": 147.068414,
        "P": 97.052764,
        "S": 87.032028,
        "T": 101.047679,
        "W": 186.079313,
        "Y": 163.06332,
        "V": 99.068414,
        }
        mass_list = [mass.get(aa,0.0)for aa in peptide]
        pep_mass=sum(mass_list)
        return pep_mass
    
    def Peptide_IPC(peptide,start_pH=6.51,Epsilon=0.01,):
        IPC_score={'Cterm': 2.383, 'pKAsp': 3.887, 'pKGlu': 4.317, 'pKCys': 8.297, 'pKTyr': 10.071, 'pk_his': 6.018, 'Nterm': 9.564, 'pKLys': 10.517, 'pKArg': 12.503}
        pKCterm = IPC_score['Cterm']
        pKAsp = IPC_score['pKAsp']
        pKGlu = IPC_score['pKGlu']
        pKCys = IPC_score['pKCys']
        pKTyr = IPC_score['pKTyr']
        pKHis = IPC_score['pk_his']
        pKNterm = IPC_score['Nterm']
        pKLys = IPC_score['pKLys'] 
        pKArg = IPC_score['pKArg']
        pH = start_pH      
        pHprev = 0.0         
        pHnext = 14.0        
        E = Epsilon  
        temp = 0.01
        nterm=peptide[0]
        cterm=peptide[-1]
    #will now cycle through all peptides until a pH within the epsilon is found       
        while 1:             
            QN1=-1.0/(1.0+pow(10,(pKCterm-pH)))                                        
            QN2=-peptide.count('D')/(1.0+pow(10,(pKAsp-pH)))           
            QN3=-peptide.count('E')/(1.0+pow(10,(pKGlu-pH)))           
            QN4=-peptide.count('C')/(1.0+pow(10,(pKCys-pH)))           
            QN5=-peptide.count('Y')/(1.0+pow(10,(pKTyr-pH)))        
            QP1=peptide.count('H')/(1.0+pow(10,(pH-pKHis)))            
            QP2=1.0/(1.0+pow(10,(pH-pKNterm)))                
            QP3=peptide.count('K')/(1.0+pow(10,(pH-pKLys)))           
            QP4=peptide.count('R')/(1.0+pow(10,(pH-pKArg)))            
            NQ=QN1+QN2+QN3+QN4+QN5+QP1+QP2+QP3+QP4

            if NQ<0.0:                                  
                temp = pH
                pH = pH-((pH-pHprev)/2.0)
                pHnext = temp

            else:
                temp = pH
                pH = pH + ((pHnext-pH)/2.0)
                pHprev = temp
            #terminal condition, finding pI with given precision defined by Epsilon
            if (pH-pHprev<E) and (pHnext-pH<E): 
                return pH
        
    def Peptide_Neutral_pH(peptide):
        z_dict = {'E': -1, 'D': -1, 'K': 1, 'R': 1} 
        charge = [z_dict.get(aa, 0.0) for aa in peptide]
        spark=sum(charge)
        return(spark)
    
    def Peptide_GRAVY(peptide):
        hydro = {     "A": 1.800,
        "R": -4.500,
        "N": -3.500,
        "D": -3.500,
        "C": 2.500,
        "Q": -3.500,
        "E": -3.500,
        "G": -0.400,
        "H": -3.200,
        "I": 4.500,
        "L": 3.800,
        "K": -3.900,
        "M": 1.900,
        "F": 2.800,
        "P": -1.600,
        "S": -0.800,
        "T": -0.700,
        "W": -0.900,
        "Y": -1.300,
        "V": 4.200,
        }
        hydro_list = [hydro.get(aa,0.0)for aa in peptide]
        hydro_sum=sum(hydro_list)
        gravy=hydro_sum/len(hydro_list)
        return gravy 
def ButcherShop(df,target,identifier,rule, min_length=7,exception=None,max_length=100, pH=2.0, min_charge=2.0,missed=0):
    pep_dict = {}
    pep_dict_list = []
    string_catcher=re.compile(r'^([A-Z]+)$')
    print(f'You order is being processed and the butcher is preparing your {rule}-cut protein(s)!')
    print("The butcher is working...")
    raw=df[[target, identifier]].set_index(identifier).to_dict()[target]
    print(f"Generating {rule}-cut peptides based on {missed}-missed cleavages. ")
    for gene,peptide in raw.items():
        pep_dict[gene] = Cleaver(peptide,rule=rule,min_length=min_length,exception=exception,missed_cleavages=missed, max_length=max_length)
    for k, lst in pep_dict.items():    
        cuts=len(lst)
        for i in range(cuts):
            d = {}
            d.update({k: lst[i]})
            d.update({'gene':k})
            d.update({'aa_comp': dict(parser.amino_acid_composition(lst[i]))})
            d.update({'peptide': lst[i]})
            d.update({'Length': len(lst[i])})
            d.update({'z': float(round(electrochem.charge(lst[i], pH=pH),3))})
            d.update({'Mass': float(Scales.Mass(lst[i]))})
            if d["z"] > 0:
                d.update({'m/z': d["Mass"]/d['z']})
            pep_dict_list.append(d)
    print("Preparing your order...")
    pep_dict_list = [peptide for peptide in pep_dict_list if peptide['z'] >= float(min_charge)]
    print(f'Order is up! You have acquired {len(pep_dict_list)} peptides that are between {min_length} and {max_length} amino acids!')
    return pep_dict_list

def Deli(z,meat_package=False):
    #z = list of dictionaries, keys must be equal thus will drop keys which are not cosistent between dictionaries
    # use after ButcherShop
    #returns dataframe
    key_intersect = set(z[0].keys()).intersection(set(z[1].keys()))
    zz = [{key:value for (key,value) in dicts.items() if key in key_intersect} for dicts in z]
    ham = pd.DataFrame(zz)
    if meat_package == True:
        ham_counts=ham.groupby('gene').size().reset_index(name='counts')
        ham=ham.merge(ham_counts,how='left', on=['gene'])
    return ham
    
#Handles Up to 3 Replicates (t_id1-3) per Selection, used for removing amino acids from N-terminal during PEAKS exports with enzyme that cleave at C-terminal. 
#Can be used to remove M from N-terminal of peptides produced by enzymes which cleave at N-terminal of target aa. 
def Butcher(df,ident1=None,ident2=None,ident3=None,t_id1=None,t_id2=None,t_id3=None,t_value=0,acid=["J","Z"],labels=list(),excel_mapper=True,excel_name=None):
    raw=df.loc[:,df.columns.str.contains(ident1)]
    tag=df[labels]
    raw = pd.concat([raw, tag], axis=1)
    raw["Peptide"]= raw["Peptide"].str.replace('\W+',"")
    raw["Peptide"]= raw["Peptide"].str.replace('\d+',"")
    raw["Peptide"]= raw["Peptide"].apply(lambda x : x[1:] if x.startswith(tuple(acid)) else x)
    cuts=raw.loc[:,raw.columns.str.contains(ident2)]
    if ident3 != None:
        cuts=cuts.loc[:,cuts.columns.str.contains(ident3)]
    cuts = pd.concat([cut, tag], axis=1)
    blade = cuts.filter(regex=r'^AREA').isin(['0']).all(axis=1)
    cuts=cuts.loc[~blade]
    cuts.reset_index(inplace=True)
    excels=[raw,cuts]
    Excel_Mapper(excels,excel_name +".xlsx")
    return raw, cuts

def Marinate (df,target,length,IPC=False,Hydro=False,GRAVY=False,NeutralZ=False,Peptide_Inspector=False):
    print("Marinating peptides...")
    if IPC is True:
        df["IPC"]=df[target].apply(Scales.Peptide_IPC)
        print("IPC calculated!")
    if GRAVY is True:
        df["Hydro_Sum"]=df[target].apply(Scales.Peptide_GRAVY)
        print("Its all GRAVY Baby!")
    if NeutralZ is True:
        df["Neutral_Z"]=df[target].apply(Scales.Peptide_Neutral_pH)
        print("Charge at Neutral pH added!")
    print("Peptides have been marinated!")
    return df

def Peptide_Inspector(df,target,new_column=None):
    all_data = []
    for peptide in df[target]:
        temp=dict(parser.amino_acid_composition(peptide))
        all_data.append(temp)
    df[new_column]=all_data
    print(f"Peptide inspection is completed! Amino acid dictionaries are stored under {new_column} in dataframe!")
    return df


def Wishbone(df,bone,split):
    x=df[bone].value_counts()
    x2=pd.DataFrame(x,columns=[bone])
    x3= x2.loc[(x2[bone])>int(split)]
    x3z=len(x3)
    x4=x3z/len(x2)*100
    print(f"The number of proteins with > {split} peptides : %.1f" % x3z)
    print(f"Ratio of Proteins with > {split} Peptides Identified: %.3f" % x4)
    return x3,x3z,x4

def Sweet_N_Sour(set1,set2):
    common_IDs=list(set(set1)&set(set2))
    common=len(common_IDs)
    unique=len(list(set(set1)^set(set2)))
    unique_set1=list(set(set1)-set(set2))
    unique_set2=list(set(set2)-set(set1))
    set1_count=len(unique_set1)
    set2_count=len(unique_set2)
    Ratio=(unique/(common+unique))*100
    print(f"The number of common peptides is: %.3f" % common)
    print(f"The number of unique peptides in set1 is: %.3f" % set1_count)
    print(f"The number of unique peptides in set1 is: %.3f" % set2_count)
    print(f"The Ratio of Unique to Common proteins is: %.3f" % Ratio)
    return common_IDs,unique_set1, unique_set2
#----------------------------------------------------------------------------------#
# Visulization Functions:

def Peptide_ICE_cloud(df,x=0,target="aa_comp"):
    word_could_dict = df[target][x]
    wordcloud = WordCloud(width = 500, height = 500,scale=10,prefer_horizontal=1,relative_scaling=1,min_font_size=18,max_font_size=48,font_step=8,
                      background_color='white',contour_width=1,contour_color="black" ).generate_from_frequencies(word_could_dict)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)

def Peptide_ICE_bar(df,x=0,target=None,lock=None,key=None):
    test_dict=df.loc[df[lock] == key][target].iloc[x]
    x=list(test_dict.keys())
    y=list(test_dict.values())
    plt.bar(x,y, color='g')

def Peptide_ICE_plot(df,x=0,target=None,lock=None,key=None):
    test_dict=df.loc[df[lock] == key][target].iloc[x]
    x=list(test_dict.keys())
    y=list(test_dict.values())
    plt.plot(x,y, color='g')

def CorrPie(df,apples,figsize=(16,8),cmap='Blues',title="Title",fontsize=18,pad=16,save_name="Heat_Test",dpi=600,fmt='eps'):
    og_corr=df[apples]
    plt.figure(figsize=figsize)
    mask=np.triu(np.ones_like(og_corr.corr(), dtype=np.bool))
    heatmap=heatmap = sns.heatmap(og_corr.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap=cmap)
    heatmap.set_title(title, fontdict={'fontsize':fontsize}, pad=pad)
    plt.savefig(save_name,format=fmt,dpi=dpi,bbox_inches="tight")
    plt.show()


def WeddingCake(df,x,y,z,dpi=300,s=12,alpha=0.3,edgecolor='k',color="blue",my_viewx=20,my_viewy=50,
               xlabel="Parameter xlabel",ylabel="Parameter ylabel",zlabel="Parameter zlabel",fmt='png',
               figx=10,figy=10,xmin=0,xmax=1000,ymin=0,ymax=1000,zmin=0,zmax=1000):
    fig = plt.figure(figsize=(figx,figy),dpi=dpi)
    ax = fig.gca(projection='3d')
    X = df[x]
    Y = df[y]
    Z = df[z]
    ax.scatter(X,Y,Z,color=color,s=s,alpha=alpha,edgecolor=edgecolor)
    ax.view_init(my_viewx,my_viewy)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.xaxis._axinfo["grid"].update({"linewidth":1, "color" : "grey"})
    ax.yaxis._axinfo["grid"].update({"linewidth":1, "color" : "grey"})
    ax.zaxis._axinfo["grid"]['color'] = "k"
    ax.zaxis._axinfo["grid"]['linestyle'] = "--"
    ax.set_ylim3d(ymin,ymax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_zlim3d(zmin,zmax)
    FigTitle=input('Figure Title:')
    plt.savefig(FigTitle,format=fmt,dpi=dpi,bbox_inches="tight")
    plt.show

def Cake(df,x,y,dpi=600,s=25,alpha=0.25,edgecolor='k',color="blue",fmt='eps',labsize=18,
               figx=10,figy=10,xmin=0,xmax=1000,ymin=0,ymax=1000,xlabel="xlabel parameter",ylabel="ylabel parameter",
        loc=2,pad=1,borderpad=1,frameon=True, show=False):
    fig, ax = plt.subplots(1,1,figsize=(figx,figy),dpi=dpi)
    X = df[x]
    Y = df[y]
    plt.scatter(X,Y,color=color,s=s, alpha=alpha,edgecolor=edgecolor)
    plt.xlabel(xlabel, fontsize=labsize)
    plt.ylabel(ylabel, fontsize=labsize)
    corr, _ = pearsonr(X, Y)
    # loc works the same as it does with figures (though best doesn't work)
    # pad=5 will increase the size of padding between the border and text
    # borderpad=5 will increase the distance between the border and the axes
    # frameon=False will remove the box around the text
    anchored_text = AnchoredText('Pearsons correlation: r = %.3f' % corr, loc=loc,pad=pad,borderpad=borderpad,frameon=frameon)
    ax.add_artist(anchored_text)
    FigTitle=input('Figure Title:')
    plt.savefig(FigTitle,format=fmt,dpi=dpi,bbox_inches="tight")

def CakePop(df,x,xi,y,yi, figx=10,figy=10,dpi=600,font_scale=1.5,figstyle="white",xlabel="xlabel",ylabel="ylabel",labsize=18,
           cmapx=-0.3,cmapy=0.0,sizex=10,sizey=200,loc='upper left',pad=1,borderpad=1,frameon=True):
    sns.set(font_scale=font_scale)
    cake=sns.set_style(figstyle)
    cmap = sns.cubehelix_palette(start=cmapx, rot=cmapy, as_cmap=True)
    X = df[x]
    Y = df[y]
    cake=sns.relplot(data=df,
    x=X, y=Y,
    hue=xi, size=yi,
    palette=cmap, sizes=(sizex, sizey))
    ax = cake.axes[0,0]
    ####
    corr, _ = pearsonr(X, Y)
    anchored_text = AnchoredText('Pearsons correlation: r = %.3f' % corr, loc=loc, prop=dict(size=labsize*0.5),pad=pad,borderpad=borderpad,frameon=frameon)
    ax.add_artist(anchored_text)
    ####
    plt.xlabel(xlabel, fontsize=labsize)
    plt.ylabel(ylabel, fontsize=labsize)
    FigTitle=input('Figure Title:')
    plt.savefig(FigTitle,format=fmt,dpi=dpi,bbox_inches="tight")
    plt.show(cake)



