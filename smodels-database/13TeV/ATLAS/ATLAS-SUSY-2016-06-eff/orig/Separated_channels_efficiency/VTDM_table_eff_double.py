import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

efficiency_files = './'

df = pd.read_csv(efficiency_files+'VTDM_double_output.dat',sep='\s+')
df = df.rename(columns={'C_Mass(GeV)':'Mass','tau(ns)':'tau','Init_xs(fb)':'xs','xs100(fb)':'xs100','total_eff':'eff','xslim(fb)':'xslim'})
df['Mass'] = df['Mass'].round(decimals=0)

df_col_to_keep = ['Mass','tau','xs','eff','xs100','xslim']
df = df[df_col_to_keep]


#taus = (df['tau']==0.01) | (df['tau']==0.05) | (df['tau']==0.1) | (df['tau']==0.5) | (df['tau']==1.0) | (df['tau']==5.0) | (df['tau']== 10.0)
taus = (df['tau']!=0.015) & (df['tau']!=0.025) & (df['tau']!=0.15) & (df['tau']!=0.25) & (df['tau']!=1.5) & (df['tau']!=2.5)


df = df[taus]
df['eff'] = df['eff'].map('{:.2e}'.format)
df['eff'] = pd.to_numeric(df['eff'])
df['xslim'] = df['xslim'].astype(float)
df['xslim'] = pd.to_numeric(df['xslim'])

#print(df.head())

#### Create pivote tables ####
table_eff = df.pivot_table(values='eff', index='tau', columns='Mass')
table_xslim = df.pivot_table(values='xslim', index='tau', columns='Mass')

tau = df['tau'].unique()
mass = df['Mass'].unique()

## Create array to fill the table
table_eff_text = []
table_xslim_text = []
for t in tau:
    val_eff=[]
    val_xslim=[]
    for m in mass:
        value_eff = df[(df['tau']==t)&(df['Mass']==m)]['eff'].values[0]
        value_xslim = df[(df['tau']==t)&(df['Mass']==m)]['xslim'].values[0]
        val_eff.append(value_eff)
        val_xslim.append(value_xslim)
    table_eff_text.append(val_eff)
    table_xslim_text.append(val_xslim)

############################################
################ table 1 ###################
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_visible(False)
plt.axis('off')
plt.axis('tight')
plt.title('Table of Efficiencies for VTDM Model \n double production channel', fontsize = 15)

cell_text = [['%.2e' % j for j in i] for i in table_eff_text]
row_labels = tau#['%.2f' % i for i in tau]
col_labels = ['%.0f' % i for i in mass]

table = plt.table(cellText=cell_text,
                  rowLabels=row_labels,
                  colLabels=col_labels,
                  colLoc='center',
                  cellLoc='center',
                  rowLoc='center',
                  loc='center',
                  colColours=np.array(['lightgrey']*len(mass)),
                  rowColours=np.array(['lightgrey']*len(tau)),
                  colWidths=np.array([0.12]*len(mass)))
table.auto_set_font_size(False)
table.set_fontsize(6.9)

##Label of axes
plt.figtext(0.06, 0.55, "Lifetime (ns)", fontsize = 12, rotation=90)
plt.figtext(0.38, 0.85, "Chargino Mass (GeV)", fontsize = 12)

fig.tight_layout()
plt.savefig('VTDM_efficiency_table_double_channel.pdf')


############################################
################# table 2 ##################
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_visible(False)
plt.axis('off')
plt.axis('tight')
plt.title('Table of cross sections limit in fb \n for VTDM Model \n double production channel', fontsize = 13)

cell_text = [['%.2e' % j for j in i] for i in table_xslim_text]
row_labels = tau#['%.2f' % i for i in tau]
col_labels = ['%.0f' % i for i in mass]

table = plt.table(cellText=cell_text,
                  rowLabels=row_labels,
                  colLabels=col_labels,
                  colLoc='center',
                  cellLoc='center',
                  rowLoc='center',
                  loc='center',
                  colColours=np.array(['lightgrey']*len(mass)),
                  rowColours=np.array(['lightgrey']*len(tau)),
                  colWidths=np.array([0.12]*len(mass)))
table.auto_set_font_size(False)
table.set_fontsize(6.5)

plt.figtext(0.06, 0.55, "Lifetime (ns)", fontsize = 12, rotation=90)
plt.figtext(0.38, 0.83, "Chargino Mass (GeV)", fontsize = 12)

fig.tight_layout()
plt.savefig('VTDM_xslim_table_double_channel.pdf')

############################################
################# table 3 ##################
df_xs = df['xs'].unique()
for i,row in enumerate(table_xslim_text):
    for j,col in enumerate(row):
       if(col < df_xs[j]):
         cell_text[i][j] = col
       else: 
         cell_text[i][j] = 0

fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_visible(False)
plt.axis('off')
plt.axis('tight')
plt.title('Accepted values for production \n cross section in VTDM Model \n for double production channel', fontsize = 13)

#cell_text = [['%.2e' % j for j in i] for i in table_xslim_text]
row_labels = tau
col_labels = ['%.0f' % i for i in mass]

table = plt.table(cellText=cell_text,
                  rowLabels=row_labels,
                  colLabels=col_labels,
                  colLoc='center',
                  cellLoc='center',
                  rowLoc='center',
                  loc='center',
                  colColours=np.array(['lightgrey']*len(mass)),
                  rowColours=np.array(['lightgrey']*len(tau)),
                  colWidths=np.array([0.12]*len(mass)))
table.auto_set_font_size(False)
table.set_fontsize(6.9)

plt.figtext(0.06, 0.55, "Lifetime (ns)", fontsize = 12, rotation=90)
plt.figtext(0.38, 0.85, "Chargino Mass (GeV)", fontsize = 12)

fig.tight_layout()
plt.savefig('VTDM_accepted_xs_points_table_double_channel.pdf')

with open('VTDM_efficiency_double_channel.tex', 'w') as f:
   f.write(table_eff.to_latex())

with open('VTDM_xslim_double_channel.tex', 'w') as f2:
    f2.write(table_xslim.to_latex())
