# Enter your code here. Read input from STDIN. Print output to STDOUT
english_news_no=int(input())
english_news_subs=set(input().split(' '))
french_news_no=int(input())
french_news_subs=set(input().split(' '))

english_only = len(english_news_subs.difference(french_news_subs))
print(english_only)
