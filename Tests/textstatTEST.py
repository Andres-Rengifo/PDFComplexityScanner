import textstat

test_data=(
"Thorne's research, initially met with skepticism, begins to yield unsettling results"
)
#factors like sentence length and syllable count per word, with shorter sentences and simpler words resulting in a higher Flesch Reading Ease score
print(textstat.flesch_reading_ease(test_data))
#This Function performs an equation that considers the average number of words per sentence
print(textstat.flesch_kincaid_grade(test_data))
#It calculates a score based on the average sentence length and the percentage of words with three or more syllables in a text sample
print(textstat.smog_index(test_data))
#set of 30 sentences from a text, count the words with three or more syllables within those sentences, take the square root of that number, and then add three
print(textstat.coleman_liau_index(test_data))
#average number of characters per word and the average number of words per sentence
print(textstat.automated_readability_index(test_data))
#to calculate the index is: "0.0588 * (letters per 100 words) - 0.296 * (sentences per 100 words) - 15.8
print(textstat.dale_chall_readability_score(test_data))
#calculates the number of complex words (criteria by textstat)
print(textstat.difficult_words(test_data))
#easy word?(1 syllable) +1 point, hard word?(2-3 syllables) +3 points, divide points by number of sentences per 100 words.
print(textstat.linsear_write_formula(test_data))
#The formula considers factors like sentence length and the number of complex words within the text. 
print(textstat.gunning_fog(test_data))
#considering various linguistic elements and providing a single score
print(textstat.text_standard(test_data))
#readability of Spanish text by analyzing the complexity of sentences and word structure
print(textstat.fernandez_huerta(test_data))
# once again for spanish texts
print(textstat.szigriszt_pazos(test_data))
#spanish text
print(textstat.gutierrez_polini(test_data))
#similar to flesch_kincaid_grade method
print(textstat.crawford(test_data))
#readability of a text based on the length of words (measured in number of letters), the number of words and the length of sentences.
print(textstat.gulpease_index(test_data))
#arabic text
print(textstat.osman(test_data))