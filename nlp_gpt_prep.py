#Pass in a Pandas Series
#Examples of how to tokenize
"""
low_pizza_ana_list = []
for x in low_pizza_ana:
  low_pizza_ana_list.append((word_tokenize(x)))
"""
#ranges will be decimals (ex. .25, .50 , .75) top 25% top 50% top 75%

def gpt_nlp_prep(df_series, top_range, mid_range, low_range):
  import nltk
  from nltk.tokenize import word_tokenize
  from nltk.corpus import stopwords
  from nltk.tokenize import sent_tokenize
  import string
  from nltk import pos_tag
  t_list = []
  for x in df_series:
    t_list.append(word_tokenize(x))  
  #Set parameters to make bi and trigrams for anagram creation function
  bigram = 2
  trigram = 3
  #lists to capture raw
  bigram_list = []
  trigram_list = []
  master_word_list = []
  #dictionaries to capture count and terms 
  bigram_dict = {}
  trigram_dict = {}
  master_word_dict = {}
  #count scale of each dictionary value
  bigram_count = []
  trigram_count = []
  master_word_count = []
  #lists to capture non-dupes
  bigram_non_dupes = []
  trigram_non_dupes = []
  master_word_non_dupes = []
  #range lists
  bigram_top_range_list = []
  bigram_mid_range_list = []
  bigram_low_range_list = []
  trigram_top_range_list = []
  trigram_mid_range_list = []
  trigram_low_range_list = []
  master_word_top_range_list = []
  master_word_mid_range_list = []
  master_word_low_range_list = []

  stop_word_list = ['both', 'myself', 'some', 'y', 'a', 'have', 'me', 'be', 'or', 'as', "shouldn't", 'by', 'but', 'they', 'you', 'same', 'yourself', 'their', 'in', 'doesn', 'm', 'at', 'why', 'when', 'further', 'not', 'my', "isn't", "shan't", 'didn', 'only', 'of', 'this', 'to', 'more', 'own', 'itself', 'ma', 'while', 's', 'theirs', 'shan', 'couldn', 'against', 'will', 'needn', 'we', 'those', 'the', 'ain', 'ourselves', 'having', 'most', 'such', 'i', 'that', 'through', "it's", "don't", "couldn't", 'off', 'being', 'it', 'mustn', 'hadn', "she's", 'before', 're', 'just', 'll', 'wouldn', 'had', "you're", "needn't", "you've", 'doing', 'she', 'there', 'him', "wouldn't", 've', "should've", "weren't", 'than', 'do', 'hers', 'all', "won't", 'he', 'up', 'how', 'after', 'and', 'our', 'herself', 'few', 'does', 'his', 'can', 't', 'were', 'below', 'don', 'about', 'isn', 'ours', 'between', 'into', 'wasn', 'has', 'o', 'am', 'which', "you'll", 'was', "hadn't", 'during', "aren't", "doesn't", 'no', 'because', 'each', "mustn't", 'down', 'these', 'yourselves', 'what', "hasn't", 'again', "didn't", "mightn't", "you'd", 'them', 'should', 'is', 'then', 'with', 'are', "that'll", 'hasn', 'out', 'who', 'aren', 'your', 'weren', 'whom', 'did', 'won', "haven't", 'its', 'over', 'd', 'above', 'until', "wasn't", 'shouldn', 'on', 'been', 'her', 'where', 'nor', 'under', 'any', 'very', 'himself', 'for', 'mightn', 'from', 'if', 'once', 'here', 'other', 'haven', 'themselves', 'too', 'an', 'now', 'yours', 'so']
  extra_punctuation_check = ["``", "''","..."] 
  my_punctuation_list = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
  bigram_dict = {}
  trigram_dict = {}
  master_word_dict = {}
  #FUNCTION TO MAKE tri and bi grams
  def anagram_creation(my_list, desired_len):
    def anagram_prep(my_list, desired_len):
      if len(my_list) % desired_len == 0:
        return my_list
      if len(my_list) % desired_len == 1:
        my_list.remove(my_list[len(my_list)-1])
        return my_list
      if len(my_list) % desired_len == 2:
        my_list.remove(my_list[len(my_list)-1])
        my_list.remove(my_list[len(my_list)-1])
        return my_list
      if len(my_list) % desired_len > 2:
        return my_list

    
    working_list = anagram_prep(my_list, desired_len)
    if desired_len == 2:
      output_list = []
      times_calculations_run = len(working_list) / 2
      my_counter = 0
      bigram_one = 0
      bigram_two = 1

      while my_counter != times_calculations_run:
        bigram_element = working_list[bigram_one] + " " + working_list[bigram_two]
        output_list.append(bigram_element)
        my_counter += 1
        bigram_one += 2
        bigram_two += 2

    if desired_len == 3:
      output_list = []
      times_calculations_run = len(working_list) / 3
      my_counter = 0
      trigram_one = 0
      trigram_two = 1
      trigram_three = 2

      while my_counter != times_calculations_run:
        trigram_element = working_list[trigram_one] + " " + working_list[trigram_two] + " " + working_list[trigram_three]
        output_list.append(trigram_element)
        my_counter += 1
        trigram_one += 3
        trigram_two += 3
        trigram_three += 3

    return output_list
  
  #bigram establishment
  for x in t_list:
    bigram_list.append(anagram_creation(x,2))

  #trigram establishment
  for x in t_list:
    trigram_list.append(anagram_creation(x,3))
  
  #bigram dictionary establishment
  for list in bigram_list:
    for x in list:
      if x not in bigram_dict:
        bigram_dict[x] = 1
      if x in bigram_dict:
        bigram_dict[x] += 1

  #trigram dictionary establishment
  for list in trigram_list:
    for x in list:
      if x not in trigram_dict:
        trigram_dict[x] = 1
      if x in trigram_dict:
        trigram_dict[x] += 1

  #Making a scale of counts of the dictionary Bigram
  for k,v in bigram_dict.items():
    bigram_count.append(v)
  

  #Making a scale of counts of the dictionary Trigram
  for k,v in trigram_dict.items():
    trigram_count.append(v)
  
  #Get rid of duplicate counts Bigram
  for x in bigram_count:
    if x not in bigram_non_dupes:
      bigram_non_dupes.append(x)
    if x in bigram_non_dupes:
      continue
  
  #Get rid of duplicate counts Trigram
  for x in trigram_count:
    if x not in trigram_non_dupes:
      trigram_non_dupes.append(x)
    if x in trigram_non_dupes:
      continue
  
  #Sort Bigrams and Trigrams
  bigram_non_dupes.sort(reverse=False)
  trigram_non_dupes.sort(reverse=False)
  
  #Bigram scales
  bigram_minimum = bigram_non_dupes[0]
  bigram_top_range = bigram_non_dupes[int(len(bigram_non_dupes) * top_range // 1)]
  bigram_mid_range = bigram_non_dupes[int(len(bigram_non_dupes) * mid_range // 1)]
  bigram_low_range = bigram_non_dupes[int(len(bigram_non_dupes) * low_range // 1)]
  bigram_maximum = bigram_non_dupes[len(bigram_non_dupes)-1]

  #Trigram scales
  trigram_minimum = trigram_non_dupes[0]
  trigram_top_range = trigram_non_dupes[int(len(trigram_non_dupes) * top_range // 1)]
  trigram_mid_range = trigram_non_dupes[int(len(trigram_non_dupes) * mid_range // 1)]
  trigram_low_range = trigram_non_dupes[int(len(trigram_non_dupes) * low_range // 1)]
  trigram_maximum = trigram_non_dupes[len(trigram_non_dupes)-1]

  #Bigram distribution to lists
  bigram_top_range_list = []
  bigram_mid_range_list = []
  bigram_low_range_list = []
  for k,v in bigram_dict.items():
    if v > bigram_minimum and v <= bigram_low_range:
      bigram_low_range_list.append(k)
    if v > bigram_low_range and v <= bigram_mid_range:
      bigram_mid_range_list.append(k)
    if v >= bigram_top_range and v <= bigram_maximum:
      bigram_top_range_list.append(k)
  
  #Trigram distribution to lists
  trigram_top_range_list = []
  trigram_mid_range_list = []
  trigram_low_range_list = []
  for k,v in trigram_dict.items():
    if v > trigram_minimum and v <= trigram_low_range:
      trigram_low_range_list.append(k)
    if v > trigram_low_range and v <= trigram_mid_range:
      trigram_mid_range_list.append(k)
    if v >= trigram_top_range and v <= trigram_maximum:
      trigram_top_range_list.append(k)
  
  #Establishing list of words
  master_word_list = []
  final_word_list = []
  clean_word_list = []
  for x in bigram_list:
    for ele in x:
      master_word_list.append(word_tokenize(ele))

  for x in master_word_list:
    for ele in x:
      final_word_list.append(ele)

  for x in final_word_list:
    if x not in stop_word_list and x not in my_punctuation_list and x not in extra_punctuation_check:
      clean_word_list.append(x)
    else:
      continue
  
  #word dictionary establishment
  for x in clean_word_list:
    if x not in master_word_dict:
      master_word_dict[x] = 1
    if x in master_word_dict:
      master_word_dict[x] += 1
  
  #Making a scale of counts of the dictionary Bigram
  for k,v in master_word_dict.items():
    master_word_count.append(v)
  
  #Get rid of duplicate counts master words
  for x in master_word_count:
    if x not in master_word_non_dupes:
      master_word_non_dupes.append(x)
    if x in master_word_non_dupes:
      continue
  
  #Sort master_words
  master_word_non_dupes.sort(reverse=False)

  #Master word scales
  master_word_minimum = master_word_non_dupes[0]
  master_word_top_range = master_word_non_dupes[int(len(master_word_non_dupes) * top_range // 1)]
  master_word_mid_range = master_word_non_dupes[int(len(master_word_non_dupes) * mid_range // 1)]
  master_word_low_range = master_word_non_dupes[int(len(master_word_non_dupes) * low_range // 1)]
  master_word_maximum = master_word_non_dupes[len(master_word_non_dupes)-1]

  #master word distribution to lists
  master_word_top_range_list = []
  master_word_mid_range_list = []
  master_word_range_list = []
  for k,v in master_word_dict.items():
    if v > master_word_minimum and v <= master_word_low_range:
      master_word_low_range_list.append(k)
    if v > master_word_low_range and v <= master_word_mid_range:
      master_word_mid_range_list.append(k)
    if v >= master_word_top_range and v <= master_word_maximum:
      master_word_top_range_list.append(k)
  top_range_output = top_range * 100
  mid_range_output = mid_range * 100
  low_range_output = low_range * 100
  

  output_dict = {(f'The top {top_range_output}% bigram') : bigram_top_range_list,
                 (f'The middle {mid_range_output}% bigram') : bigram_mid_range_list,
                 (f'The low {low_range_output}% bigram') : bigram_low_range_list,
                 (f'The top {top_range_output}% trigram') : trigram_top_range_list,
                 (f'The middle {mid_range_output}% trigram') : trigram_mid_range_list,
                 (f'The low {low_range_output}% trigram') : trigram_low_range_list,
                 (f'The top {top_range_output}% words') : master_word_top_range_list,
                 (f'The middle {mid_range_output}% words') : master_word_mid_range_list,
                 (f'The low {low_range_output}% words') : master_word_low_range_list,
  }
  """
  output = [(f'The top {top_range_output}% bigram : {bigram_top_range_list} '),
  (f'The middle {mid_range_output}% bigram : {bigram_mid_range_list} '),
  (f'The low {low_range_output}% bigram : {bigram_low_range_list}'),
  (f'The top {top_range_output}% trigram : {trigram_top_range_list} '),
  (f'The middle {mid_range_output}% trigram : {trigram_mid_range_list} '),
  (f'The low {low_range_output}% trigram : {trigram_low_range_list}'),
  (f'The top {top_range_output}% words : {master_word_top_range_list} '),
  (f'The middle {mid_range_output}% words : {master_word_mid_range_list} '),
  (f'The low {low_range_output}% words : {master_word_low_range_list}')
   ]
  """



  return output_dict
