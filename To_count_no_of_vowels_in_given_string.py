#11.To_count_no_of_vowels_in_given_string
str1=input()
count=0
for i in str1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count=count+1
print(count)