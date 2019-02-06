import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    
    input_file = open(sentiment_file, 'r')
    for line in input_file:
       div1 = line.split('\t' )
       scores[div1[0]] = int(div1[1])
    
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    
    div3 = tweet.split( )
    num = len(div3)
    for i in range(0,num):
        if div3[i] in sent_scores:
            score = score+sent_scores[div3[i]]
    
    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    input_file = open(tweets_file,'r')
    for line in input_file:
        div = line.split()
        num = len(div)
        for i in range(0,num):
            if div[i] in sent_scores:
                pass
            elif div[i] in new_term_sent:
                new_term_sent[ div[i] ] = new_term_sent[ div[i] ] + get_tweet_sentiment( line, sent_scores )
            else:
                new_term_sent[ div[i] ] =  get_tweet_sentiment( line, sent_scores )
            
    
    
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()