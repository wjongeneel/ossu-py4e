text = "X-DSPAM-Confidence:    0.8475"
start_index = text.find('0')
end_index = text.find('5') + 1
print(float(text[start_index:end_index]))