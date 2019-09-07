import os, sys, time

class colors:
    GREEN = '\033{92m'
    YELLOW = '\033{93m'
    RED = '\033[91m'










os.system('Title Setitune Moderator Application Program')
print(colors.RED + 'Welcome to Setitune.')
time.sleep(1)
os.system('cls')
print(colors.RED + 'If you have not already, please join the discord: https://discord.gg/yX9GSHB')
os.system('pause')
os.system('cls')
print(colors.RED + 'First Question, How much are you online?')
print(colors.RED + '[1]All the time')
print(colors.RED + '[2]Most of the time')
print(colors.RED + '[3]Usually')
print(colors.RED + '[4]Rarely')
print(colors.RED + '[5]Never')
print(' ')
Question1Answer = input(colors.RED + 'Answer: ')

os.system('cls')
print(colors.RED + 'Second Question, how long have you been exploiting, please choose the closest one.')
print(colors.RED + '[1]One Month')
print(colors.RED + '[2]Three Months')
print(colors.RED + '[3]Six Months')
print(colors.RED + '[4]1 Year')
print(colors.RED + '[5]2 Years')
print(colors.RED + '[6]3 Years')
print(colors.RED + '[7]5 Years')
print(colors.RED + '[8]5+ Years')
print(' ')
Question2Answer = input(colors.RED + 'Answer: ')

os.system('cls')
print(colors.RED + 'Third Question, how well do you think you know RLua (ROBLOXs programming language)?')
print(colors.RED + '[1]Very well')
print(colors.RED + '[2]Quite well')
print(colors.RED + '[3]Good')
print(colors.RED + '[4]Quite good')
print(colors.RED + '[5]Beginner')
print(colors.RED + '[6]Very little')
print(colors.RED + '[7]None')
print(' ')
Question3Answer = input(colors.RED + 'Answer: ')









os.system('cls')
print(colors.RED + '[1]Submit')
print(colors.RED + '[2]Cancel')
print(' ')
SubmitAnswer = input(colors.RED + 'Option: ')
if SubmitAnswer == '1':
    if Question1Answer == '1':
        Question1Answer = 'na28sinmfaop2m'
    if Question1Answer == '2':
        Question1Answer = 'asjfamn2infsks'
    if Question1Answer == '3':
        Question1Answer = 'sfaiksnjmndwjf'
    if Question1Answer == '4':
        Question1Answer = 'sfjandnwjnafkj'
    if Question1Answer == '5':
        Question1Answer = 'aknsdni2nflska'

    if Question2Answer == '1':
        Question2Answer = 'sfajsndjwnajkf'
    if Question2Answer == '2':
        Question2Answer = 'snfajksdjnwkan'
    if Question2Answer == '3':
        Question2Answer = 'fjskanjknwdjfn'
    if Question2Answer == '4':
        Question2Answer = 'asnfjkadjnwajk'
    if Question2Answer == '5':
        Question2Answer = 'ruygfjsdksjnej'
    if Question2Answer == '6':
        Question2Answer = 'sanfwjdjfjrgkf'
    if Question2Answer == '7':
        Question2Answer = 'usjdnjwkfjnsaj'
    if Question2Answer == '8':
        Question2Answer = 'pfsdnajnkjgrse'

    if Question3Answer == '1':
        Question3Answer = 'rugskdnfkjsnej'
    if Question3Answer == '2':
        Question3Answer = 'runfjdsjknkjfn'
    if Question3Answer == '3':
        Question3Answer = 'gdrgdhjfdgrgfh'
    if Question3Answer == '4':
        Question3Answer = 'kjuygtyfrgdfgs'
    if Question3Answer == '5':
        Question3Answer = 'gfdrgwsefdhgfd'
    if Question3Answer == '6':
        Question3Answer = 'wfdgsdgfdhtfth'
    if Question3Answer == '7':
        Question3Answer = 'jdrgsdfasdffhf'



    print(colors.RED + 'Please contact Etrath#1983 on Discord.')
    file = open('Answers.txt', 'w')
    file.write('Question 1:\n[1]All the time\n[2]Most of the time\n[3]Usually\n[4]Rarely\n[5]Never\n' + '\n' + '\n' + '\n' + '\n' + 'Question 2:\n[1]One Month\n[2]Three Months\n[3]Six Months\n[4]1 Year\n[5]2 Years\n[6]3 Years\n[7]5 Years\n[8]5+ Years\n' + '\n' + '\n' + '\n' + 'Question 3:\n[1]Very well\n[2]Quite well\n[3]Good\n[4]Quite good\n[5]Beginner\n[6]Very little\n[7]None\n' + '\n' + '\n' + '\n' + 'Question 1 Answer: ' + Question1Answer + '\nQuestion 2 Answer: ' + Question2Answer + '\nQuestion 3 Answer: ' + Question3Answer)
    file.close()

    os.system('pause')
else:
    sys.exit(0)

time.sleep(5555)
