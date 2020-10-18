import pickle
f=open('consolidate_Twitter.pickle','wb')
l=['ss_trials_215353','ss_trials_215941','ss_trials_22215','ss_trials_22251','ss_trials_222625','ss_trials_222625','ss_trials_22282','ss_trials_223017','ss_trials_223114','ss_trials_223423','ss_trials_224026','ss_trials_224554','ss_trials_225116','ss_trials_225726','ss_trials_23240','ss_trials_23811','ss_trials_231358','ss_trials_232013','ss_trials_232528','ss_trials_233137','ss_trials_233749','ss_trials_234249','ss_trials_234919','ss_trials_235420','ss_trials_0029','ss_trials_0633','ss_trials_01127','ss_trials_01722','ss_trials_02255','ss_trials_0298','ss_trials_03519','ss_trials_0419','ss_trials_04640','ss_trials_05254','ss_trials_05854','ss_trials_150',
'ss_trials_150','ss_trials_11027','ss_trials_11634','ss_trials_12249','ss_trials_12834','ss_trials_1343','ss_trials_13954','ss_trials_14625','ss_trials_15212','ss_trials_15824','ss_trials_2413','ss_trials_2109','ss_trials_21539','ss_trials_21539','ss_trials_22159','ss_trials_22740','ss_trials_2343','ss_trials_24115','ss_trials_2463','ss_trials_25242','ss_trials_25810','ss_trials_3419','ss_trials_3102','ss_trials_31538','ss_trials_32147','ss_trials_32753','ss_trials_33432','ss_trials_34015','ss_trials_34625','ss_trials_35226','ss_trials_35829','ss_trials_4356','ss_trials_4104','ss_trials_41553','ss_trials_42219','ss_trials_4283','ss_trials_4349','ss_trials_44044','ss_trials_44535','ss_trials_45147','ss_trials_45747','ss_trials_5311','ss_trials_5926','ss_trials_51525','ss_trials_52129','ss_trials_52746','ss_trials_53334','ss_trials_53922','ss_trials_54526','ss_trials_55153','ss_trials_5585','ss_trials_6337','ss_trials_6929','ss_trials_6154','ss_trials_62119','ss_trials_62718','ss_trials_63259','ss_trials_63855','ss_trials_64449','ss_trials_65020','ss_trials_65628','ss_trials_721','ss_trials_7813','ss_trials_71414','ss_trials_72019','ss_trials_72614','ss_trials_73113','ss_trials_73744','ss_trials_75511','ss_trials_8039','ss_trials_8658','ss_trials_82417','ss_trials_82927','ss_trials_84751','ss_trials_85912','ss_trials_9447'
,'ss_trials_91035','ss_trials_91642','ss_trials_92236','ss_trials_94534','ss_trials_10843','ss_trials_101446','ss_trials_102031','ss_trials_102625','ss_trials_10327','ss_trials_103810']
l=[i +'.pickle' for i in l]

for i in l:
    nf=open(i,'rb')
    while 1:
        try:
            a=pickle.load(nf)
            pickle.dump(a,f)
        except EOFError:
            print('over')
            break
    nf.close()
    
            
            
        
    
