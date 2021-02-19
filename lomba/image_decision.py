class decision:
    def __init__(self):
        self.distance_enemies = 0

    def distance_calib(self, distance_ball,distance_enemies,distance_goal,cnts1_b,cnts2_b,cnts1_e,cnts2_e,cnts1_g,cnts2_g):
        if distance_enemies <10:
            distance_enemies=0
        elif distance_enemies >1000:
            distance_enemies = 0
            
        if distance_ball <10:
            distance_ball=0
        elif distance_ball >1000:
            distance_ball=0
        
        if distance_goal <40:
            distance_goal=0
        elif distance_goal >1000:
            distance_goal=0
        
        if len(cnts1_b) <= 0 or len(cnts2_b) <= 0:
            distance_ball=0
        
        if len(cnts1_e) <= 0 or len(cnts2_e) <= 0:
            distance_enemies=0

        if len(cnts1_g) <= 0 or len(cnts2_g) <= 0:
            distance_goal=0
        return distance_ball, distance_enemies, distance_goal

    
    def straight_condition_edit_gagal(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
        if 112<=mx1_b<=220 and 73<=mx2_b<=182 and 83<=my1_b<=220:#50-100cm
            cond = 1
            print("maju 50-100cm")
        elif 124<=mx1_b<=205 and 97<=mx2_b<=176 and 50<=my1_b<=82 : # 100-150
            cond = 1
            print("maju 100-150")
        elif 135<=mx1_b<=186 and 107<=mx2_b<=176 and 36<=my1_b<=49 : #160-200
            cond = 1
            print("maju 160-200")
        elif 136<=mx1_b<=183 and 119<=mx2_b<=165 and 22<=my1_b<=35: #210-250
            cond = 1
            print("maju 210-250")
        elif 139<=mx1_b<=179 and 126<=mx2_b<=166 and 0<=my1_b<=21: #260-300
            cond = 1
            print("maju 260-300")
        elif mx1_b>215 and mx2_b>177 and 83<=my1_b<=220: #50-100
            cond = 0
            print("kanan 50-100")
        elif mx1_b>199 and mx2_b>198 and 50<=my1_b<=171 : #110-150
            cond = 0
            print("kanan 110-150")
        elif mx1_b>181 and mx2_b>159 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kanan 160-200")
        elif mx1_b>178 and mx2_b>161 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kanan 210-250")
        elif mx1_b>174 and mx2_b>160 and 0<=my1_b<=21: #260-300
            cond = 0
            print("kanan 210-300")
        elif mx1_b<117 and mx2_b<65 and 78<=my1_b<=220: #50-100
            cond = 0
            print("kiri 50-100")
        elif mx1_b<129 and mx2_b<102 and 50<=my1_b<=82 : #110-150
            cond = 0
            print("kiri 110-150")
        elif mx1_b<140 and mx2_b<119 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kiri 160-200")
        elif mx1_b<141 and mx2_b<124 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kiri 210-250")
        elif mx1_b<144 and mx2_b<131 and 0<my1_b<=21: #260-300
            cond = 0
            print("kiri 210-300")
        else:
            cond = 0
            print("uncondition")
        return cond
    def straight_condition(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
        
        if 117<=mx1_b<=215 and 78<=mx2_b<=177 and 83<=my1_b<=220:#50-100cm
            cond = 1
            print("maju 50-100cm")
        elif 129<=mx1_b<=200 and 102<=mx2_b<=171 and 50<=my1_b<=82 : # 100-150
            cond = 1
            print("maju 100-150")
        elif 140<=mx1_b<=181 and 102<=mx2_b<=171 and 36<=my1_b<=49 : #160-200
            cond = 1
            print("maju 160-200")
        elif 141<=mx1_b<=178 and 124<=mx2_b<=161 and 22<=my1_b<=35: #210-250
            cond = 1
            print("maju 210-250")
        elif 144<=mx1_b<=174 and 131<=mx2_b<=160 and 0<=my1_b<=21: #260-300
            cond = 1
            print("maju 260-300")
        elif mx1_b>215 and mx2_b>177 and 83<=my1_b<=220: #50-100
            cond = 0
            print("kanan 50-100")
        elif mx1_b>199 and mx2_b>198 and 50<=my1_b<=171 : #110-150
            cond = 0
            print("kanan 110-150")
        elif mx1_b>181 and mx2_b>159 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kanan 160-200")
        elif mx1_b>178 and mx2_b>161 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kanan 210-250")
        elif mx1_b>174 and mx2_b>160 and 0<=my1_b<=21: #260-300
            cond = 0
            print("kanan 210-300")
        elif mx1_b<117 and mx2_b<65 and 78<=my1_b<=220: #50-100
            cond = 0
            print("kiri 50-100")
        elif mx1_b<129 and mx2_b<102 and 50<=my1_b<=82 : #110-150
            cond = 0
            print("kiri 110-150")
        elif mx1_b<140 and mx2_b<119 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kiri 160-200")
        elif mx1_b<141 and mx2_b<124 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kiri 210-250")
        elif mx1_b<144 and mx2_b<131 and 0<my1_b<=21: #260-300
            cond = 0
            print("kiri 210-300")
        # elif len(cnts1_b) > 0 and len(cnts2_b) <= 0:
        #     print("kiri")
        #     cond = 2
        # elif len(cnts1_b) <= 0 and len(cnts2_b) > 0:
        #     print("kanan")
        #     cond = 3
        else:
            cond = 0
            print("uncondition")
        return cond

    def enemies_condition(self,mx1_e,mx2_e,cnts1_e,cnts2_e,distance_enemies):
        #enemies_on_the_mid_or_not
        if 155<=mx1_e<=227 and 110<=mx2_e<=177 and 130<=my1_e<=204:
            enemies_cond = False
        elif 165<=mx1_e<=200 and 139<=mx2_e<=165 and 65<=my1_e<=129:
            enemies_cond = False
        elif 170<=mx1_e<=185 and 151<=mx2_e<=166 and my1_e<65:
            enemies_cond = False
        else:
            enemies_cond = True
        
        if len(cnts1_e) <= 0 and len(cnts2_e) <= 0:
            enemies_cond2 = True
        elif len(cnts1_e) > 0 and len(cnts2_e) > 0 and distance_enemies >100:
            enemies_cond2 = True
        else:
            enemies_cond2 = False
        
    def straight_condition_old(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
            
        if 126<=mx1_b<=252 and 65<=mx2_b<=202 and 83<=my1_b<=220:#50-100cm
            cond = 1
            print("maju 50-100cm")
        elif 135<=mx1_b<=230 and 97<=mx2_b<=198 and 50<=my1_b<=82 : # 100-150
            cond = 1
            print("maju 100-150")
        elif 151<=mx1_b<=219 and 126<=mx2_b<=195 and 36<=my1_b<=49 : #160-200
            cond = 1
            print("maju 160-200")
        elif 161<=mx1_b<=215 and 143<=mx2_b<=194 and 22<=my1_b<=35: #210-250
            cond = 1
            print("maju 210-250")
        elif 164<=mx1_b<=208 and 149<=mx2_b<=192 and 0<=my1_b<=21: #260-300
            cond = 1
            print("maju 260-300")
        elif mx1_b>252 and mx2_b>202 and 83<=my1_b<=220: #50-100
            cond = 0
            print("kanan 50-100")
        elif mx1_b>230 and mx2_b>198 and 50<=my1_b<=82 : #110-150
            cond = 0
            print("kanan 110-150")
        elif mx1_b>219 and mx2_b>195 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kanan 160-200")
        elif mx1_b>215 and mx2_b>194 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kanan 210-250")
        elif mx1_b>208 and mx2_b>192 and 0<=my1_b<=21: #260-300
            cond = 0
            print("kanan 210-300")
        elif mx1_b<126 and mx2_b<65 and 83<=my1_b<=220: #50-100
            cond = 0
            print("kiri 50-100")
        elif mx1_b<135 and mx2_b<97 and 50<=my1_b<=82 : #110-150
            cond = 0
            print("kiri 110-150")
        elif mx1_b<151 and mx2_b<126 and 36<=my1_b<=49: #160-200
            cond = 0
            print("kiri 160-200")
        elif mx1_b<161 and mx2_b<143 and 22<=my1_b<=35: #210-250
            cond = 0
            print("kiri 210-250")
        elif mx1_b<164 and mx2_b<149 and 0<my1_b<=21: #260-300
            cond = 0
            print("kiri 210-300")
        # elif len(cnts1_b) > 0 and len(cnts2_b) <= 0:
        #     print("kiri")
        #     cond = 2
        # elif len(cnts1_b) <= 0 and len(cnts2_b) > 0:
        #     print("kanan")
        #     cond = 3
        else:
            cond = 0
            print("uncondition")
        return cond

    def straight_condition_1(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
        if len(cnts1_b)<=0 or len(cnts2_b)<=0:
            cond = 0
        elif 158<mx1_b<208:
            cond = 1
            # print("tengah banget")
        elif 125<=mx1_b<=158 and ((((-mx1_b+158)/33)*150)+90)<my1_b: 
            cond = 2
            # print("tengah kiri")
        elif 208<=mx1_b<=275 and ((((-mx1_b+208)/-67)*150)+90)<my1_b: 
            cond = 3
            # print("tengah kanan")     
        elif 125<=mx1_b<=158 and ((((-mx1_b+158)/33)*150)+90)>my1_b: 
            cond = 2
            # print("kiri mendekati tengah")
        elif 208<=mx1_b<=275 and ((((-mx1_b+208)/-67)*150)+90)>my1_b: 
            cond = 3
            # print("kanan mendekati tengah")   
        elif 0<=mx1_b<125:
            cond = 2 
            # print("kiri")     
        elif 275<mx1_b<=320:
            cond = 3 
            # print("kanan")     
        else:
            cond = 0
            # print("uncondition")
        return cond
    
    def straight_condition_2(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
        if len(cnts1_b)<=0 or len(cnts2_b)<=0:
            cond = 0
        elif 162<mx1_b<180:
            cond = 1
            #print("tengah banget")
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)<my1_b: 
            cond = 1
            #print("tengah kiri")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)<my1_b: 
            cond = 1
            #print("tengah kanan")     
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)>my1_b: 
            cond = 2
            #print("kiri mendekati tengah")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)>my1_b: 
            cond = 3
            #print("kanan mendekati tengah")   
        elif 0<=mx1_b<128:
            cond = 2
            #print("kiri")     
        elif 249<mx1_b<=320:
            cond = 3 
            #print("kanan")     
        else:
            cond = 0
            #print("uncondition")
        return cond

        
    def straight_condition_3(self, mx1_b,mx2_b, my1_b,my2_b,cnts1_b,cnts2_b):
        if len(cnts1_b)<=0 or len(cnts2_b)<=0:
            cond = 0
        # elif mx1_b == 0:
        #     cond = 0
        if 162<mx1_b<180:
            cond = 1
            #print("tengah banget")
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)<my1_b: 
            cond = 1
            #print("tengah kiri")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)<my1_b: 
            cond = 1
            #print("tengah kanan")     
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)>my1_b: 
            cond = 2
            #print("kiri mendekati tengah")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)>my1_b: 
            cond = 3
            #print("kanan mendekati tengah")   
        elif 0<=mx1_b<128:
            cond = 4
            #print("kiri")     
        elif 249<mx1_b<=320:
            cond = 5 
            #print("kanan")     
        else:
            cond = 0
            #print("uncondition")
        return cond
    
    def straight_condition_4(self, mx1_b, my1_b,cnts1_b,):
        if len(cnts1_b)<=0:
            cond = 0
        elif mx1_b == 0:
            cond = 0
        elif 162<mx1_b<180:
            cond = 1
            #print("tengah banget")
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)<my1_b: 
            cond = 1
            #print("tengah kiri")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)<my1_b: 
            cond = 1
            #print("tengah kanan")     
        elif 128<=mx1_b<=162 and (((-mx1_b+162)*(150/34))+90)>my1_b: 
            cond = 2
            #print("kiri mendekati tengah")
        elif 180<=mx1_b<=249 and (((-mx1_b+180)*(150/-69))+90)>my1_b: 
            cond = 3
            #print("kanan mendekati tengah")   
        elif 0<=mx1_b<128:
            cond = 4
            #print("kiri")     
        elif 249<mx1_b<=320:
            cond = 5 
            #print("kanan")     
        else:
            cond = 0
            #print("uncondition")
        return cond
    
    def straight_condition_letfhi(self, mx1_b, my1_b,cnts1_b,):
        if len(cnts1_b)<=0:
            cond = 0
        elif mx1_b == 0:
            cond = 0
        elif 163<mx1_b<181:
            cond = 1
            #print("tengah banget")
        elif 107<=mx1_b<=163 and (((-mx1_b+107)*(174/56))+240)<my1_b: 
            cond = 1
            #print("tengah kiri")
        elif 181<=mx1_b<=243 and (((-mx1_b+243)*(-174/62))+240)<my1_b: 
            cond = 1
            #print("tengah kanan")     
        elif 107<=mx1_b<=163 and (((-mx1_b+107)*(174/56))+240)>my1_b: 
            cond = 2
            #print("kiri mendekati tengah")
        elif 181<=mx1_b<=243 and (((-mx1_b+243)*(-174/62))+240)>my1_b: 
            cond = 3
            #print("kanan mendekati tengah")   
        elif 0<=mx1_b<112:
            cond = 2
            #print("kiri")     
        elif 242<mx1_b<=320:
            cond = 3 
            #print("kanan")     
        else:
            cond = 0
            #print("uncondition")
        return cond

    def straight_condition_jasmine(self, mx1_b, my1_b,cnts1_b,):
        if len(cnts1_b)<=0:
            cond = 0
        elif mx1_b == 0:
            cond = 0
        elif 168<mx1_b<184:
            cond = 1
            #print("tengah banget")
        elif 112<=mx1_b<=168 and (((-mx1_b+112)*(159/56))+240)<my1_b: 
            cond = 1
            #print("tengah kiri")
        elif 184<=mx1_b<=242 and (((-mx1_b+242)*(-159/58))+240)<my1_b: 
            cond = 1
            #print("tengah kanan")     
        elif 112<=mx1_b<=168 and (((-mx1_b+112)*(159/56))+240)>my1_b: 
            cond = 2
            #print("kiri mendekati tengah")
        elif 184<=mx1_b<=242 and (((-mx1_b+242)*(-159/58))+240)>my1_b: 
            cond = 3
            #print("kanan mendekati tengah")   
        elif 0<=mx1_b<112:
            cond = 2
            #print("kiri")     
        elif 242<mx1_b<=320:
            cond = 3 
            #print("kanan")     
        else:
            cond = 0
            #print("uncondition")
        return cond
        