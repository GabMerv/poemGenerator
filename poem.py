import random
import sys
import io
from random import choice, randint
import roman
from googletrans import Translator
def convertRomain(nb):
   return roman.toRoman(nb)


def getRime(chain, lookedFor):
   if len(lookedFor)>=4:
      lastLetters = lookedFor[-4:-1]
      rimes = []
      for word in chain:
         if len(word) >= 4:
            if word.endswith(lastLetters) and word != lookedFor:
               rimes.append(word)
      if not rimes:
         return None
      rime = choice(rimes)
      def recursiveVerse(chain, word, message):
         if word.capitalize() == word:
            message.append(word)
            return message
         else:
            possWord = []
            possKey = []
            for key in chain:
               if word in chain[key]:
                  possWord.append(word)
                  possKey.append(key)
            i = randint(0, len(possKey)-1)
            word = possKey[i]
            message.append(possWord[i])

            return recursiveVerse(chain, word, message)
      mot = recursiveVerse(chain, rime, [])
      if len(mot) >=2:
         return mot
      else:
         return None

def createTitre(num, chain, message):
   w = ''
   msg = message[0].split("\n")
   tab = []
   for el in msg:
      tab.extend(el.split(" "))
   while len(w) <6:
      w = choice(tab)
   if w[-1] == ",":
      w = w[0:-1]
   titre = ['{} - {}\n'.format(num, w.capitalize())]
   titre.extend(message)
   return titre

def sonnet(chain):
   message = []
   for i in range(2):
      message.append(createCoplet(chain, 4))
   for i in range(2):
      message.append(createCoplet(chain, 2))
   return message

def randomForm(chain):
   message = []
   for i in range(randint(2, 5)):
      message.append(createCoplet(chain, randint(2, 8)))
   return message

def haiku(chain):
   message = []
   message.append(createCoplet(chain, 3))
   return message

def oneStanza(chain):
   message = []
   message.append(createCoplet(chain, randint(4, 10)))
   return message

def twoStana(chain):
   message = []
   message.append(createCoplet(chain, 2))
   return message

def createCoplet(chain, count):
   word1 = random.choice(list(chain.keys()))
   message = word1.capitalize()
   while len(message.split("\n"))<=count:
      def first(chain, word1):
         try:
            word2 = random.choice(chain[word1])
            return word2
         except:
            return first(chain, word1)
      word2 = first(chain, word1)
      word1 = word2
      if message[-1] != '\n':
         message += ' ' + word2
      else:
         if word2:
            if word2[0] in [",", ";", ":", ".", '!', "?", "-", " "]:
               word2 = word2[2:-1]
            message += word2
      if len(message.split("\n"))>=1:
         try:
            if word2[-1] in [",", ";", ":", ".", '!', "?", "-"] and len(message.split("\n")[-1])>=20:
               msg = getRime(chain, word2)
               message += "\n"
               if msg:
                  msg = msg[::-1]
                  message += " ".join(msg)
                  message += '\n'
         except:
            pass
   msg = message.lower()
   msg = msg.split("\n")
   for i in range(len(msg)):
      msg[i] = msg[i].capitalize()
   return message

with io.open("data.txt",'r',encoding='utf8') as f:
   poems = f.read()
   poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n", " ").split(' ')
   index = 1
   chain = {}
   message = []
   for word in poems[index:]:
      key = poems[index - 1]
      if key in chain:
         chain[key].append(word)
      else:
         chain[key] = [word]
      index += 1
   reccueil = []
   for i in range(100):
      form = randint(0, 4)
      message = []
      if form == 0:
         message = sonnet(chain)
      if form == 1:
         message = randomForm(chain)
      if form == 2:
         message = haiku(chain)
      if form == 3:
         message = oneStanza(chain)
      if form==4:
         message = twoStana(chain)
      message = createTitre(convertRomain(i+1), chain, message)
      message = "\n".join(message)
      reccueil.append(message)









author = "Baudelaire"
titre = 'Les fleurs du mal'
print(titre)
print("\n")
print("--------------\n\n".join(reccueil))
print(author)
transl = Translator()
