class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 0           # COUNTER TO GET RES
        rest = nums[0]      # TAKE 1ST NUM AND ITERATE OVER REST
        incflag = False     #FLAG TO TRACK INCREMENT
        decflag = False     #FLAG TO TRACK DECREMENT
        for i in nums[1:]:
            if i>rest and not incflag:      #IF POSITIVE DEFLECTION MAKE INC FLAG TRUE AND DEC FLAG FALSE AND VICE VERSA
                rest = i                    #MAKE REST TO CURRENT TO COMPARE NEXT
                count+=1                    #INCREMENT COUNTER
                incflag = True
                decflag = False
            elif i<rest and not decflag:    #SAME AS ABOVE
                rest = i
                count+=1
                incflag = False
                decflag = True
            else:                           #IF 3,5,7,6  AFTER 5 INC FLAG IS TRUE AND 7 COMES (IE) WE CAN'T ADD COUNTER 
                rest = i                    #BUT CAN UPDATE REST TO MAX POSIBLE ELEMENT TO DETECT NEXT DEC SO CAN DIRECTLY ASSIGN REST = 7
        return count+1                      #SO CAN DECTECT 6<7 LATER BETER TO UPDATE MAX TO REST COMPARISION VICEVERSA
                                            #INCASE 3,5,2 IT AUTOMATICALLY GO TO ELIF SAME FOR DECREMENT ALSO SO WE USE THIS ELSE
            
        