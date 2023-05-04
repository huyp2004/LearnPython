class analysedText(object):
    
    def __init__(self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        self.text = text.lower()
        
        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = self.text.replace('.', '').replace('!', '').replace(',', '').replace('?', '')
    
    def freqAll(self):

        # TODO: Create a dictionary with the unique words in the text as keys
        my_dict = {}
        self.fmtText = self.fmtText.split()
    
        # and the number of times they occur in the text as values
        for key in self.fmtText:
            my_dict[key] = self.fmtText.count(key)
        # return the created dictionary
        return my_dict
    
    def freqOf(self, word):
        my_self = self.freqAll()

        if word in my_self:
            return my_self[word]
        else:
            return 0


a = analysedText("Phan. Ngyuen. Quoc! Huy., huy Ngay hom nay toi mua dien thoai, ha ha ha ha")

print(a.freqOf("ha"))
