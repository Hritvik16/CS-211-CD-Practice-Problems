class ScoreList(list):
    def __init__(self, scores):
        if not all(isinstance(x, (int, float)) for x in scores):
            raise ValueError("All elements must be numbers")
        super().__init__(scores)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("ScoreLists must be of equal length")
        return ScoreList([a * b for a, b in zip(self, other)])

class Gradebook:
    def __init__(self, score_lists):
        if not score_lists:
            self.averages = []
            return
        num_tests = len(score_lists[0])
        for sl in score_lists:
            if len(sl) != num_tests:
                raise ValueError("All ScoreLists must have same length")
        self.averages = []
        for i in range(num_tests):
            col = [sl[i] for sl in score_lists]
            self.averages.append(sum(col) / len(col))

if __name__ == "__main__":
    s1 = ScoreList([80, 90, 100])
    s2 = ScoreList([70, 85, 95])
    gb = Gradebook([s1, s2])
    print(gb.averages)
    print(s1 * s2)
