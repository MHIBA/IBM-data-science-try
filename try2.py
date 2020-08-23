    #Conditional Statements
#x = input("enter the x")
    #10 un yanindaki : yi unutma
#if x < 10:
    #print("bigger")
#if x > 20:
    #print("smaller")
#print("finis")

#en sol satira sequential (sirali) kod, icerdekine

#Nested Decisions
#x = input ("enter the x")
#if x >1 :
    #print("more than one")
    #if x<100:
        #print ("less than 100")
#if x<=0:
    #print("less than one")
#print("all done")

#esittir isareti saga yazilir



#else (two way decisions)iki secenekten birini secme (degilse gibi)

#hava durumuna gore evde kalma yada disari cikma programi
#x = input("wheather")

#if x<23:
    #print("stay at home")
#else :
    #print ("go out")
#print("all done")

#elif (multiway decision making)
#gpslerde kullaniliyormus, else ve if in birlesimidir.

#elif asaidaki degerine 1 yazildiginda islevini gerceklestir.
# cunku 1 hem 10 dan hem de 2 den kucuktur bizim istegimiz mediumun 2 ile 10 arasinda olmasidir.
# bunun icin elif kullaniriz.

#x = input("size")

#if x<2:
    #print("small")
#elif x<10:
    #print("medium")
#else :
    #print ("large")
#print("all done")

#debuger:Kodun normal calisip calismadigini kontrol ediyor.

#astr = "Bob"

#try:
    #print("Hello")
    #istr = int(astr)
    #print ("there")
#except:
    #istr = -1

#print("done",istr)

#bu kod blow up oldu
#def greet (lang):
    #if lang == "es":
        #return "Hola"
    #elif lang == "fr":
        #print "bonjour"
    #else:
        #return "hello"
#print ("greet(fr)")


#while repeated caselerde kullanuliyor.
#repeated ststementslerde infinite loop a girmememk icin "break" kelimesei kullanilir.

#a simple definite loop
#for i  in [1,2,3,4,5]:
    #print (i)
#print ("blastoff")


#Finding Largest Value

#largest_so_far = -1
#print("before","largest_so_far")
#for the_num in [9,41,12,3,74,15]:
    #if the_num > largest_so_far :
        #largest_so_far =the_num
    #print (largest_so_far,the_num)

#print ("After","largest_so_far")


#Counting in a Loop

#zork = 0
#print ("Before",zork)
#for thing in [9, 41, 12, 3, 74, 15]:
    #zork = zork + 1
    #print (zork, thing)

#print ("after",zork)

#Summing in a loop

#zork = 0
#print ("before",zork)
#for thing in [9, 41, 12, 3, 74, 15]:
    #zork = zork + thing
    #print (zork, thing)

#print ("After", zork)




#Finding the average in the loop

#count = 0
#sum = 0
#print ("Before", "count", "sum")
#for value in [9, 41, 12, 3, 74, 15]:
    #count = count + 1
    #sum = sum + value

#print ("after", count, sum, sum/count)


#Filtering in a Loop

#print ("Before")
#for value in [9, 41, 12, 3, 74, 15]:
    #if value > 20 :
        #print "Large_number", value

#print ("After", value)


#searchig using a boolean variable


#Boolean is a kind of variable that either has the value True or False,
# that's it, it can only have two.

#found = "false"
#print ("Before", found)
#for value in [9, 41, 12, 3, 74, 15] :
    #if  value == 3 :
         #found = "true"
    #print (found, value)
#print ("after", found)


#HOW TO FIND SMALLEST VALUE

#"none"nin yerine -1 yazmistik ama -1 yada herhangi bir sayi kodumuz icin buyuk kavramini doldurmayabilir.
#bunun icin onun yerine none yazdik.
#none i value ye esitledik, ama esitlerken "is" kullanildi. Bu esittir isarettinden daha gucludur.
#"none" ya "flag value" deniliyor.
#"is" not also logical operator, bur stronger than "="

#smallest = "none"
#for value in [9, 41, 12, 3, 74, 15]:
    #if smallest is "none":
        #smallest = value
    #elif value < smallest:
        #smallest = value
    #print (smallest, value)

#print ("after", smallest)

num = 0
tot = 0.0

while True :
     sval = input("Enter a number:")
     if sval == "done":
        break
     try :
        fval = float("sval")
     except :
         print("invalid input")
         continue
     #print "fval"
     num = num + 1
     tot = tot + fval

print("ALL DONE")
#print("tot","num","tot/num")


