import library as lb
name = []
mother_name = []
name_sum = 0
mother_name_sum = 0
print("\t............................................")
print("\t:   እንኳን ወደ ስነ-ከዋክብት ካልኩሌተር በደህና መጡ::    :")
print("\t............................................")
for n in input("\n\tየእርስዎን ስም ያስገቡ : "):
     name.append(n)
for m in input("\n\tየእናትዎን ስም ያስገቡ : "):
     mother_name.append(m)
for i in name:
	for j in lb.fidel_value_pair().keys():
		for k in j:
			if k==i:
				name_sum = (name_sum + lb.fidel_value_pair()[j])%12 # 12 is standard value we use to calculate astrology sign
for i in mother_name:
	for j in lb.fidel_value_pair().keys():
		for k in j:
			if k == i:
				mother_name_sum=(mother_name_sum+lb.fidel_value_pair()[j])%12
total_sum = (name_sum + mother_name_sum)%12
title_list = list(lb.kokeb_disc_pair().keys())
print(f"\n\t-----------------------------------\n\n\tየእርስዎ ኮከብ'{title_list[total_sum-1]}'ነው::")
cont=input("\n\tስለ ኮከብዎ ማወቅ ይፈልጋሉ?  ['አዎ','አይ']\n\n\t")

if cont =='አዎ':
	print(f"\n\t.........................\n\t:'{title_list[total_sum-1]}'  :\n\t.........................\n\n")
	specific_title = title_list[total_sum-1]
	title_info = lb.kokeb_disc_pair()[specific_title]
	new_info_list = title_info.split()
# the logic below is just to customize the look of the text,it does'nt affect the value of the result.
	for i in range(len(new_info_list)):
	    if i != 8 and i%10==8:
	    	print(new_info_list[i],"\n\n\t",end=" ")
	    else:
	       print(new_info_list[i],end=" ")
print("\n\n")
