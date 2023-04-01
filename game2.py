story={1:{"text" : "You stand on the beach of a deserted island.", "options": [{1:'walk into the jungle', "jumpto": 2},{2: "follow the beach", "jumpto": 3},{3:"explore plane wreck", "jumpto":4}]},
   2:{"text" : "You walk up to the tree line and into the jungle. The Air is very humid and you hear the chirping of birds and insects.", "options": [{1:"listen to the noises.", "jumpto": 2},{2: "follow the beach", "jumpto": 3},{3:"explore plane wreck", "jumpto":4}]},
   3:{"text" : "You choose to follow the beach and after walking for a while, you come across a small stream that flows into the ocean.", "options": [{1:'You can choose to follow the stream', "jumpto": 5},{2: "or continue walking along the beach", "jumpto": 6}]},
   4:{"text" : "You stand on the beach of a deserted island.", "options": [{1:'walk into the jungle', "jumpto": 2},{2: "follow the beach", "jumpto": 3},{3:"explore plane wreck", "jumpto":4}]}}

def main(ch_id):
   text = story[ch_id]
   print(text["text"])
   print("What do you want to do next?")
   i=1
   for option in text["options"]:
      print(i, " : ",option[i])
      i+=1
   choice = input("Type number of choice: ")
   main(int(choice))

if __name__ == '__main__':
   main(1)