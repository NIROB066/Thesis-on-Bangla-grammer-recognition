'''
Took an example of
3
S->A S B
A->a A S|a|epsilon
B->S b S|A|b b

S0->S
S → AS|ASB| SB| S
A → aAS|aS|a
B → SbS| A|bb


8
S->NP VP
NP->PRONOUN NOUN
NP->ADJ ADJ NOUN|NOUN NP
VP->NOUN VERB
PRONOUN->আমি
NOUN->সকাল|টিকিট
ADJ->দশটার|প্লেনের
VERB->চাই

8
S->NP VP
NP->PRONOUN NOUN
NP->ADJ NOUN|NOUN NP
VP->NOUN VERB
PRONOUN->আমি
NOUN->সকাল|টিকিট
ADJ->দশটার|প্লেনের
VERB->চাই


6
S->AA BB|বীর|MANGO AA
AA->শূন্য|কি
BB->কি
MANGO->S AA
P->S BB
NIROB->AA AA
বীর কি শূন্য
S


7
S->NP VP|VP NP|NP S|NOUN VP|NP VERB
PRONOUN->আমি
NOUN->সকাল|টিকিট
ADJ->দশটার|প্লেনের|ADJ ADJ
VERB->চাই
NP->ADJ NOUN|NOUN ADJ|PRONOUN NOUN|NP ADJ|NP NP|NOUN NP|NP NOUN
VP->NOUN VERB|ADJ VP|NP VERB
আমি সকাল দশটার প্লেনের টিকিট চাই
S


7
S->NP VP|VP NP|NP S
PRONOUN->আমি
NOUN->সকাল|টিকিট
ADJ->দশটার|প্লেনের|ADJ ADJ
VERB->চাই
NP->ADJ NOUN|NOUN ADJ|PRONOUN NOUN|NP ADJ|NP NP
VP->NOUN VERB|ADJ VP
আমি সকাল দশটার প্লেনের টিকিট চাই
S

8
S->NP VP|VP NP|NP S|NOUN VP|NP VERB
PRONOUN->আমি
NOUN->সকাল|টিকিট
ADV->দশটায়
ADJ->প্লেনের
VERB->চাই
NP->PRONOUN NOUN|NOUN ADV|ADJ NOUN|NOUN NP
VP->ADV VERB|VERB ADJ|NP VERB|VP ADJ|VERB NP
আমি সকাল দশটায় চাই প্লেনের টিকিট
S
'''
#For Bangla
from bijoy2unicode import converter
#For Bangla
# Tkinter APP code
def clear_widget(widget1,widget2):
    widget1.destroy()
    widget2.destroy()
label0=""
import tkinter as tk

root = tk.Tk()
large_font = ('Kalpurush ANSI', 30)

canvas1 = tk.Canvas(root, width=800, height=750, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Bangla Language Pattern Detection')
label1.config(font=('Times', 18, 'bold', 'italic'))
canvas1.create_window(400, 75, window=label1)

label2 = tk.Label(root, text='Type your Input sentence (বাংলাতে):')
label2.config(font=('helvetica', 14))
canvas1.create_window(400, 150, window=label2)

entry1 = tk.Entry(root, width=30, bd=5, font=large_font)

canvas1.create_window(400, 210, window=entry1)
# Tkinter app code

from tabulate import tabulate


def epsilon_remove(i_val):  # Removes "epsilon" productions
    non_terminal = inp_gram[i_val].split("->")  # non_terminal[0] will contain for which nonterminal "epsilon" comes
    for length in range(len(inp_gram)):
        production = inp_gram[length]  # S->ASB comes in production
        rhs = production.split("->")  # rhs[1] will contain aAs|a
        all_rhs = rhs[1].split("|")  # all_rhs will contain "aAs", "a"
        for all_rhs_len in range(len(all_rhs)):
            if all_rhs[all_rhs_len].find(non_terminal[0]) != -1:  # if "A" finds in aAS
                if len(all_rhs[all_rhs_len]) == 1:  # if it is "A", replaces with "epsilon"
                    inp_gram[length] = rhs[0] + "->"
                    for al in range(len(all_rhs)):
                        inp_gram[length] += all_rhs[al] + "|"
                    inp_gram[length] += "epsilon"
                else:
                    temp = all_rhs[all_rhs_len]
                    replc = all_rhs[all_rhs_len].index(non_terminal[0])  # Detecting index of non-terminal A
                    inp_gram[length] = inp_gram[length] + "|" + temp[:replc] + temp[
                                                                               replc + 2:]  # for A->a A S, replc will be 2;temp[:replc] will be"a ";temp[replc+2:] will be "S"
                    if replc + 2 > len(temp) - 1:  # If "B" to be replaced from "A S B"; we will have "A S "
                        temp = inp_gram[length]
                        inp_gram[length] = temp[:len(temp) - 1]  # reduct extra space from "A S "; result is "A S"


def unit_production_reduction(single_production,
                              val_i):  # B->A ; these type of production will be replaced by A → a A S|a S|a ; result B->a A S|a S|a
    for search in range(len(inp_gram)):
        left_side = inp_gram[search].split("->")
        if single_production == left_side[0]:
            inp_gram[val_i] += left_side[1] + "|"
            return left_side[1]
            break


# Now we will remove duplicate products
# This will make S->AS|aAS|AS|aAS to S->AS|aAS
# This function first takes all the unique products in list_of_unique_productions[] then resolves
# This should be optimized because not every production rule has duplicacy
# I will  work here later Aroni , remember me please
def remove_duplicate(val_i):
    list_of_unique_productions = []
    r8_of_inp_gram = inp_gram[val_i].split("->")
    products = r8_of_inp_gram[1].split("|")
    for up in range(len(products)):
        if products[up] not in list_of_unique_productions:
            list_of_unique_productions.append(products[up])
    inp_gram[val_i] = r8_of_inp_gram[0] + "->"
    for u in range(len(list_of_unique_productions)):
        inp_gram[val_i] += list_of_unique_productions[u] + "|"
    tmp1 = inp_gram[val_i]
    inp_gram[val_i] = tmp1[:len(tmp1) - 1]


# Starting main program
# reading from file
con = [
    '8 ',
	'S->NP VP|NP Wh|NP Aux Adjective|NP Wh VP|NP VP Aux|Wh NP VP|Adverb VP ',
    'NP->Pronoun Noun|Det Noun|Pronoun NP|Pronoun Aux|Adjective Noun|Adjective NP|NP NP|Noun Noun|Noun|NP Noun|Noun Aux|NP Aux|Noun Aux Noun|NP Aux Noun|Pronoun NP|NP Adjective|Pronoun|Pronoun Aux Pronoun|Pronoun Aux Adjective Noun|Pronoun Aux NP|Pronoun Wh|Wh Noun|Pronoun Wh Noun|Wh Noun Noun|Pronoun Wh NP|Wh Noun Pronoun|Pronoun Adjective Noun|Modifier Noun|Pronoun Modifier Noun|Noun Adjective Noun|Noun Modifier Noun|Pronoun Modifier Noun|Noun NP|Noun Aux NP|Noun Aux Adjective Noun|Adjective Det Noun|Pronoun Aux Pronoun|Pronoun Aux Pronoun Noun|Pronoun Noun Adjective Noun|Pronoun Aux NP|Pronoun Aux Noun|Pronoun Aux Pronoun Noun|Pronoun Pronoun|Pronoun Pronoun Noun|Pronoun Noun Noun|Pronoun Noun Wh|NP Wh|Pronoun Noun Wh|Noun Conj Noun|Pronoun Conj Noun|Pronoun Conj Pronoun|Pronoun Noun Conj Noun|Adjective Noun Wh|Adjective Noun Conj|Adjective Noun Adjective Noun|Noun Adjective Noun Conj|Noun Pronoun Conj Pronoun|Noun Pronoun Adjective|Noun Noun Conj Pronoun|Noun Noun Conj Pronoun|Pronoun Adjective|Pronoun Pronoun conj Pronoun|Modifier Conj Adjective|Noun Pre Noun|Noun Pre|Adjective Noun ',
	'VP->IV TV|Noun IV|TV|Adverb TV|TV Aux|Adjective Noun TV|Noun TV|Noun Noun TV|Adverb IV|IV IV TV|Noun Aux Adverb IV|Adverb IV IV TV|Adverb IV IV|Adjective Noun Aux Adverb IV|Noun Aux Adverb IV IV|Noun Aux Adverb IV|Pronoun IV|Wh Noun Pronoun IV|Noun TV|Adjective Noun TV|Modifier Noun TV|Adjective Noun IV|Noun VP|Noun IV TV|Noun Adjective Noun IV|TV Aux|VP Aux|IV TV Aux|Adverb TV Aux|Noun Adjective Noun IV|Wh TV|Adverb TV|Noun Conj Noun IV|Pronoun Aux VP|Noun IV TV Neg|Noun TV Neg|TV Neg|Noun TV Adverb|IV TV Adverb|Pronoun Adjective TV|Pronoun IV TV Neg|Noun TV TV|Pronoun TV TV|Pronoun TV TV Neg|TV Adjective Noun|IV TV Adjective Noun|TV Adjective Pronoun|IV TV Adjective Pronoun|Adjective Noun TV Neg|Adjective TV ',
	'Adjective->Adj|Adjective Adj ',
	'Pronoun->আমি|আপনাদের|আপনি|আমাকে|আপনার|আমি|আমাকে|আমার ',
	'Aux->কি ',
	'Adverb->দেরি|এখন|দুপুরে|বিকালে|রাতে|নাস্তার|আজকে|উপরে ',
	'Noun->টিকেট|টিকিট|সিট|আসন|হ্যান্ডক্যারি|মালামাল|মূল্য|সার্ভিস|ব্যবস্থা|অনলাইনে|অনলাইন|ফ্লাইট|সিটবেল্ট|শ্রেণী|শ্রেণি|ক্লাস|সময়|খাবার|বিমানে|বিমান|পরিবহন|পরিবহনে|কার্ড|পাসপপোর্ট|বাগপত্র|ব্যাগ|থলে|বালিশ|কম্বল|ঘন্টা|শনিবার|রবিবার|সোমবার|মঙ্গলবার|বুধবার|বৃহস্পতিবার|শুক্রবার|সময়সূচি|দাম|ঢাকা|খুলনা|সিলেট|চট্টগ্রাম|বরিশাল|রংপুর|যশোরসৈয়দপুর|রাজশাহী ',
	'S '
]
print("Number of productions please : ")
n = int(con[0])  # Number of productions
inp_gram = []  # Here we store all the production rules
new_production_rules = []  # Here new rules will be added
mapping = {}  # Here terminals will be mapped to corresponding non-terminal,for example...S->aAS|aa|AS to S->XAS|XX|AS... "a" will be mapped to "X" here
counter = 0  # For mapping to terminals, like Xk=X0; Xk=x1. so, Xk->a,Xk->b equivalent to X0->a,X1->b and so on.
print("Grammer please : ")
for i in range(1, n + 1):
    temp_s = con[i]
    inp_gram.append(temp_s[0:len(temp_s) - 1])  # inp_gram will contain all the productions; this is a list
s0 = inp_gram[0].split('->')  # S->ASB will be splited into S and ASB
inp_gram.append("S0->" + s0[0])  # S0->S will be appended
# We will start removing "epsilon" productions now
while 1:
    chk = 0
    for i in range(len(inp_gram)):
        if inp_gram[i].find(
                "epsilon") != -1:  # if "epsilon" found call epsilon_remove with for which production "epsilon" found
            chk = 1
            new = inp_gram[i].replace("epsilon", "")  # "epsilon" removed from the production
            inp_gram.remove(inp_gram[i])  # production contains "epsilon" removed from the cfg
            if new[len(new) - 1] == "|":
                new = new[:len(new) - 1]  # if '|' remains in production, remove it
                inp_gram.append(new)  # "epsilon" and '|' removed production is added to cfg again
            else:
                inp_gram.append(new)  # "epsilon" removed production is added to cfg again
            epsilon_remove(len(inp_gram) - 1)
            break
    if chk == 0:
        break

# Now we will start removing unit productions
is_done = 1
while is_done == 1:
    is_done = 0
    for i in range(len(inp_gram)):
        r8_side = inp_gram[i].split("->")  # r8_side[1] will be "A S B|S B|A S|S" from "S->A S B|S B|A S|S"
        r8_split = r8_side[1].split("|")  # r8_split will be "A S B","S B","A S","S"
        for j in range(len(r8_split)):
            r8_split_split = r8_split[j].split(" ")
            if len(r8_split_split) == 1 and r8_split[j] >= "A" and r8_split[j] <= "Z":
                inp_gram[i] = r8_side[0] + "->"
                for k in range(len(r8_split)):
                    if k != j:
                        inp_gram[i] = inp_gram[i] + str(r8_split[k]) + "|"
                    else:
                        is_done = 1
                        r8_split[k] = unit_production_reduction(r8_split[k],
                                                                i)  # sending unit production and production number
        tmp = inp_gram[i]
        while tmp[len(tmp) - 1] == "|":
            inp_gram[i] = tmp[:len(tmp) - 1]  # removing "|" from end of productions
            tmp = tmp[:len(tmp) - 1]
        remove_duplicate(i)

# Now we will remove nonterminals which are with terminals and more than one terminals

for i in range(len(inp_gram)):
    two_part = inp_gram[i].split("->")
    products = two_part[1].split("|")
    for j in range(len(products)):
        string1 = products[j]
        string2 = products[j]
        string2_split = string2.split(" ")
        if len(string2_split) > 1:
            for k in range(len(string2_split)):
                if string2_split[k] >= 'ক' and string2_split[k] <= 'ৎ' or string2_split[k] >= 'অ' and string2_split[
                    k] <= 'ঔ':
                    if string2_split[k] not in mapping:
                        mapping.update({"X" + str(counter): string2_split[k]})
                        string2 = string2.replace(string2_split[k], "X" + str(counter))
                        # print(string2)
                        counter += 1
                    else:
                        string2 = string2.replace(string2_split[k], mapping[string2_split[k]])
                        # print(string2)
        two_part[1] = two_part[1].replace(products[j], string2)
    inp_gram[i] = two_part[0] + "->" + two_part[1]

# Now we will make s->ASB to S->XB; X->AS
for i in range(len(inp_gram)):
    two_part = inp_gram[i].split("->")
    products = two_part[1].split("|")
    for j in range(len(products)):
        single_product = products[j].split(" ")
        original_product = products[j]
        while len(single_product) >= 3:
            string = single_product[0] + " " + single_product[1]

            products[j] = products[j].replace(string, "X" + str(counter))
            mapping.update({"X" + str(counter): string})
            counter += 1
            single_product = products[j].split(" ")
        two_part[1] = two_part[1].replace(original_product, products[j])
    inp_gram[i] = two_part[0] + "->" + two_part[1]

for x, y in mapping.items():
    inp_gram.append(x + "->" + y)
# print(inp_gram)

# Now lets start CYK Algorithm
import numpy as ARRAY

cnf_store = ARRAY.zeros((10000, 100),
                        dtype=object)  # we'll store like S->A B|a like this; cnf_store[0][0]=S; [0][1]=A; [0][2]=B; [0][3]=a.
for i in range(len(inp_gram)):
    k = 0  # We want to store [][k], [][k+1] ... in cnf_store
    fst_div = inp_gram[i].split("->")  # S->A B|a will split into S and A B|a
    cnf_store[i][k] = fst_div[0]  # S is going to cnf_store[0][0]
    k += 1  # next we want to put in [][1] location
    snd_div = fst_div[1].split("|")  # "A B|a" will be "A B" and "a"
    for j in range(len(snd_div)):
        cnf_store[i][k] = snd_div[j]
        k += 1


# print(cnf_store)
# Now we'll receive input from you in bangla.
# APP
def getinput():
    xxx1 = entry1.get()
    test = converter.Unicode()
    xxx1 = test.convertBijoyToUnicode(xxx1)

    temporary = len(xxx1)
    while (1):
        if xxx1[temporary - 1] == " ":
            xxx1[temporary - 1] == "";
            temporary -= 1;
            xxx1 = xxx1[0:temporary]
        else:
            break
    xxx1 += " "
    print("Give the input language...")
    input_sentence = xxx1.split(" ")
    for_tabular_show = xxx1  # To show in tabular form
    print("Give start symbol...")
    st = con[n + 1]
    cnf_table = ARRAY.zeros((len(input_sentence) + 2, len(input_sentence)), dtype=object)
    for i in range(1, len(input_sentence)):
        positions = ARRAY.argwhere(cnf_store == input_sentence[i - 1])
        m = []  # latest change
        if len(positions) > 0:
            m = []
            for j in range(len(positions)):
                m.append(cnf_store[positions[j][0]][0])
        cnf_table[1][i] = m
    for j in range(2, len(input_sentence)):
        sol1 = 1
        for i in range(j, len(input_sentence)):
            tp = []
            temp = []
            for k in range(1, j):
                dif_with_j = j - k
                l1 = (cnf_table[k][sol1])
                l2 = (cnf_table[dif_with_j][k + sol1])
                if len(str(l1)) and len(str(l2)) != -99999999999:

                    for l1_i in range(len(l1)):
                        for l2_i in range(len(l2)):
                            string_new = l1[l1_i] + " " + l2[l2_i]
                            # print("This is new str:", string_new)
                            p = ARRAY.argwhere(cnf_store == string_new)
                            # print("This is P:",p)
                            if len(p) > 0:
                                for p_i in range(len(p)):
                                    tp = cnf_store[p[p_i][0]][0]
                                    # temp += tp
                                    temp.append(tp)
                                    # print("This is temp: ",temp)
                    # Delete duplicates
                    temp = list(dict.fromkeys(temp))
                    cnf_table[j][sol1] = temp
                    # print("This is tempFinal: ", temp)
            sol1 += 1
    # for showing in tabular from we do it
    print(for_tabular_show)
    inp_sen = for_tabular_show
    inp_sen_sp = inp_sen.split(" ")
    print(tabulate(cnf_table[1:len(input_sentence), 1:], headers=inp_sen_sp, tablefmt='orgtbl'))
    # print(cnf_table[0:len(input_sentence)])
    start_symbol = st[0]
    # output_sentence
    output_sentence = "Input is NOT correct!"
    if start_symbol in cnf_table[len(input_sentence) - 1][1]:
        output_sentence = "Input is correct!"
        print("Input is correct!")
    label3 = tk.Label(root, text='The Parsing result is ', font=('helvetica', 14, 'bold'))
    canvas1.create_window(400, 310, window=label3)

    label4 = tk.Label(root, text=tabulate(cnf_table[1:len(input_sentence), 1:], headers=inp_sen_sp, tablefmt='grid'),
                      font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 440, window=label4)

    label5 = tk.Label(root, text=output_sentence, font=('helvetica', 14, 'bold',))
    canvas1.create_window(400, 590, window=label5)

    button2 = tk.Button(root, text="Clear", command=lambda: clear_widget(label4,label5), bg='brown', fg='white',font=('helvetica', 12, 'bold'), width=20)
    canvas1.create_window(510, 270, window=button2)



button1 = tk.Button(text='Click Me', command=getinput, bg='brown', fg='white', font=('helvetica', 12, 'bold'), width=20)
canvas1.create_window(300, 270, window=button1)







root.mainloop()



