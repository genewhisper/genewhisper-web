import sqlite3
import pandas
from pathogenicity import gvit_categorizers
from pathogenicity import gvit_pathogenicity

# exec(open('db_util.py').read())

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
print('Connection successful')

df1 = pandas.read_sql('select * from  pathogenicity_oncotatoroutput', connection)
df2 = pandas.read_sql('select * from  pathogenicity_pathogenicity', connection)
df2.drop('oncotatoroutput_id', axis=1)

df2['PVS1'] = df1.apply(lambda item: gvit_categorizers.PVS1(item), axis=1)

df2['PM1'] = df1.apply(lambda item: gvit_categorizers.PM1(item), axis=1)
df2['PM2'] = df1.apply(lambda item: gvit_categorizers.PM2(item), axis=1)
df2['PM3'] = df1.apply(lambda item: gvit_categorizers.PM3(item), axis=1)
df2['PM4'] = df1.apply(lambda item: gvit_categorizers.PM4(item), axis=1)
df2['PM5'] = df1.apply(lambda item: gvit_categorizers.PM5(item), axis=1)
df2['PM6'] = df1.apply(lambda item: gvit_categorizers.PM6(item), axis=1)

df2['PS1'] = df1.apply(lambda item: gvit_categorizers.PS1(item), axis=1)
df2['PS2'] = df1.apply(lambda item: gvit_categorizers.PS2(item), axis=1)
df2['PS3'] = df1.apply(lambda item: gvit_categorizers.PS3(item)[0], axis=1)
df2['PS4'] = df1.apply(lambda item: gvit_categorizers.PS4(item), axis=1)

df2['PP1'] = df1.apply(lambda item: gvit_categorizers.PP1(item), axis=1)
df2['PP2'] = df1.apply(lambda item: gvit_categorizers.PP2(item), axis=1)
df2['PP3'] = df1.apply(lambda item: gvit_categorizers.PP3(item), axis=1)
df2['PP4'] = df1.apply(lambda item: gvit_categorizers.PP4(item), axis=1)
df2['PP5'] = df1.apply(lambda item: gvit_categorizers.PP5(item), axis=1)

df2['BP1'] = df1.apply(lambda item: gvit_categorizers.BP1(item), axis=1)
df2['BP2'] = df1.apply(lambda item: gvit_categorizers.BP2(item), axis=1)
df2['BP3'] = df1.apply(lambda item: gvit_categorizers.BP3(item), axis=1)
df2['BP4'] = df1.apply(lambda item: gvit_categorizers.BP4(item), axis=1)
df2['BP5'] = df1.apply(lambda item: gvit_categorizers.BP5(item), axis=1)
df2['BP6'] = df1.apply(lambda item: gvit_categorizers.BP6(item), axis=1)
df2['BP7'] = df1.apply(lambda item: gvit_categorizers.BP7(item), axis=1)

df2['BS1'] = df1.apply(lambda item: gvit_categorizers.BS1(item), axis=1)
df2['BS2'] = df1.apply(lambda item: gvit_categorizers.BS2(item), axis=1)
df2['BS3'] = df1.apply(lambda item: gvit_categorizers.BS3(item), axis=1)
df2['BS4'] = df1.apply(lambda item: gvit_categorizers.BS4(item), axis=1)

df2['BA1'] = df1.apply(lambda item: gvit_categorizers.BA1(item), axis=1)
df2['Google_Scholar'] = df1.apply(lambda item: gvit_categorizers.PS3(item)[1], axis=1)

df2.to_sql('pathogenicity_pathogenicity', connection, if_exists="replace", index=False)

df3 = pandas.read_sql('select * from  pathogenicity_pathogenicity', connection)
df3.drop('oncotatoroutput_id', axis=1)

df3['Pathogenicity'] = df3.apply(lambda item: gvit_pathogenicity.pathogenicity(item)[0], axis=1)
df3['Pathogenicity_Rule'] = df3.apply(lambda item: gvit_pathogenicity.pathogenicity(item)[1], axis=1)

df3.to_sql('pathogenicity_pathogenicity', connection, if_exists="replace", index=False)

connection.close()
