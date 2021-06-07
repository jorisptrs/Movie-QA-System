




def get_q_list():

	lines = open('all_qs.csv', 'r', encoding='utf8').readlines()
	questions = []
	for line in lines:
		line=line.strip()
		http_start_pos = line.find('http')
		if http_start_pos == -1:
			http_start_pos = line.find('wikidata')
		if http_start_pos == -1:
			http_start_pos = line.find('?')+1

		q = line[:http_start_pos].strip()
		words = line.split('\t')
		ans_pos = 0
		for i in range(len(words)):
			word = words[i]
			if word.startswith('https'):
				ans_pos = i+1
				break
		answers = words[ans_pos:]
		answers = [ans for ans in answers if '://www.wikidata.org/' not in ans]
		questions.append((q, answers))
	return questions
