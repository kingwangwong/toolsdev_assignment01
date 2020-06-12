import nltk
import newspaper
from newspaper import news_pool

blnd_paper = newspaper.build('https://www.blenderguru.com/')
awn_paper = newspaper.build('https://www.awn.com/')
crbl_paper = newspaper.build('https://www.creativebloq.com/')

#papers = [blnd_paper, awn_paper, crbl_paper]
#news_pool.set(papers, threads_per_source=2) 
#news_pool.join()


def keywords_in_article(text):
	b_article = blnd_paper.articles[0]
	b_article.download()
	b_article.parse()
	b_article.nlp()
	for article in blnd_paper.articles:
		if text in blnd_paper.text:
			print(blnd_paper.summary)
	with open('news_summary.txt', 'w') as reader:
		writer.write(article.title, article.author, article.summary)



userinput = input("Please enter any keyword(press enter to continue):")
print(keywords_in_article(userinput))

