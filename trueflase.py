questions_list = [
    {"question": "The sun is a planet.", "answer": False},
    {"question": "Water boils at 100 degrees Celsius.", "answer": True},
    {"question": "The Great Wall of China is visible from space.", "answer": False},
    {"question": "Albert Einstein was a famous musician.", "answer": False},
    {"question": "The Statue of Liberty was a gift from France.", "answer": True},
    {"question": "The capital of Japan is Tokyo.", "answer": True},
    {"question": "The Great Barrier Reef is located in Africa.", "answer": False},
    {"question": "Mars is the fourth planet from the sun.", "answer": True},
    {"question": "The Earth is flat.", "answer": False},
    {"question": "Pablo Picasso was a famous painter.", "answer": True}
]


class Questions:

    def __init__(self):
        self.score = 0

    def next(self,que,ans,u_ans):
        
        self.answer = ans
        self.question = que
        self.unserans = u_ans

        if ans != u_ans :
            self.score += 1
            print(f"Current score is : {self.score}")
        else:
            print("wrong ans")

for questions in questions_list :
    quest_list =questions["question"]
    ans_list = questions["answer"]
    print(f"There are {len(questions_list)} Questions to ans:")
    user_ans =input(f" Q .{quest_list} (True/Flase) ? ")
    quest =Questions()
    quest.next(quest_list,ans_list,user_ans)



