import hashlib
import json
import uuid



def main():
	with open('sentences.txt', 'r', encoding='utf-8', newline='\n') as f:
		text = f.read()

	blocks = text.strip().split('\n\n')
	if not blocks:
		print('No sentences to mine.')
		exit(1)

	sentences = []

	for block in blocks:
		block = block.strip()

		if not block:
			continue

		parts = block.split('\n')

		if len(parts) != 5:
			print(f'The sentence block starting with the following line is not valid, as it has {len(parts)} instead of 5:\n{parts[0]}')
			continue

		term, sentence, termTranslation, sentenceTranslation, definition = parts
		blockHash = hashlib.sha512(block.encode('utf-8')).hexdigest()

		sentences.append({
			'id': uuid.uuid4().hex,
			'term': term,
			'sentence': sentence,
			'termTranslation': termTranslation,
			'sentenceTranslation': sentenceTranslation,
			'definition': definition,
			'hash': blockHash,
		})

	print(f'Found {len(sentences)} valid sentence blocks.')

	with open('sentences.json', 'w', encoding='utf-8', newline='\n') as f:
		json.dump(sentences, f, indent='\t')


if __name__ == "__main__":
	main()
