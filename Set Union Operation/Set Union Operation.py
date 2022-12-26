# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_news_no=int(input())
english_news_subs=set(input().split(' '))
french_news_no=int(input())
french_news_subs=set(input().split(' '))

at_least_one_sub = len(english_news_subs.union(french_news_subs))
print(at_least_one_sub)
