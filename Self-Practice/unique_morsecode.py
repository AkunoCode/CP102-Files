class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dict = dict(zip("abcdefghijklmnopqrstuvwxyz", [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                          "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]))

        morse_set = set()
        for word in words:
            morse_set.add("".join([morse_dict[letter]for letter in word]))

        return len(morse_set)
