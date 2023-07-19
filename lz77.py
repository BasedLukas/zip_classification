

class LZ77Compressor:
    """
    A simplified implementation of the LZ77 Compression Algorithm
    Modified from this code here:
    https://github.com/manassra/LZ77-Compressor
    """

    def __init__(self, window_size=50, lookahead_buffer_size=15):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, input):

        data = input
        i = 0
        output = []

        while i < len(data):
            match = self.findLongestMatch(data, i)
            if match:
                (bestMatchDistance, bestMatchLength) = match
                output.append((bestMatchDistance, bestMatchLength, data[i + bestMatchLength]))
                i += bestMatchLength + 1
            else:
                output.append((0,0,data[i]))
                i += 1
        return output

    def decompress(self, input):
        output = []
        for item in input:
            if item[0] == 0 and item[1] == 0:
                output.append(item[2])
            else:
                start = len(output) - item[0]
                for i in range(item[1]):
                    output.append(output[start + i])
                output.append(item[2])
        return ''.join(output)

    def findLongestMatch(self, data, current_position):
        """ 
        Finds the longest match to a substring starting at the current_position 
        in the lookahead buffer from the history window
        """
        end_of_buffer = min(current_position + self.lookahead_buffer_size, len(data) + 1)

        best_match_distance = -1
        best_match_length = -1

        for j in range(current_position + 2, end_of_buffer):

            start_index = max(0, current_position - self.window_size)
            substring = data[current_position:j]

            for i in range(start_index, current_position):

                repetitions = len(substring) // (current_position - i)

                last = len(substring) % (current_position - i)

                matched_string = data[i:current_position] * repetitions + data[i:i+last]

                if matched_string == substring and len(substring) > best_match_length:
                    best_match_distance = current_position - i 
                    best_match_length = len(substring)

        if best_match_distance > 0 and best_match_length > 0:
            return (best_match_distance, best_match_length)
        return None



