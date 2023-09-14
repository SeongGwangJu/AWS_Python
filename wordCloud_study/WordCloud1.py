import wordcloud as wc

text = "python python test data user wordcloud 파이썬"
wcText = wc.WordCloud(font_path="c\\Windows\\Fonts\\맑은 고딕\\malgun.ttf",
                        background_color="white",
                        stopwords=["test", "data"],
                        min_font_size = 10,
                        max_font_size = 25,
                        width=800,
                        height=900)

wcText.generate_from_text(text)
# wcText.to_image().show()

##이미지 저장
wcText.to_file("test3.png")
