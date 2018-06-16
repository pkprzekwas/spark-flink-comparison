
def combine_filter(word):
    return [word, word.lower(), word.title(), word.upper()]


programming_filters = [
    *combine_filter('Python'),
    *combine_filter('Java'),
    *combine_filter('C#'),
    *combine_filter('Ruby'),
    *combine_filter('Scala'),
    *combine_filter('JavaScript'),
    *combine_filter('Java Script'),
]
