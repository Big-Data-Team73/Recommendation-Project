import json


business_id_set = set()
user_id_set = set()
user_review_rating_sum_dict = {}
user_review_count_dict = {}
CURRENT_CITY = 'Las Vegas'      # select all businesses in a city

# "business_id", "full_address", "hours", "open", "categories" ,"city" ,"review_count" , "name", "neighborhoods", |
# "longitude", "state", "stars", "latitude", "attributes":, "type"


def data_constructor():
    dataset = open('yelp_academic_dataset_business.json', 'r')

    for line in dataset:
        line_dict = json.loads(line)
        bcity = line_dict['city'].encode('utf-8')
        if bcity != CURRENT_CITY:
            continue
        if str(line_dict['categories']).find('Restaurants') != -1:
            bid = line_dict['business_id'].encode('utf-8')
            business_id_set.add(bid)

    dataset.close()

# "votes", "user_id", "review_id", "stars", "date", "text", "type", "business_id"

    dataset = open('yelp_academic_dataset_review.json', 'r')
    output = {}
    for line in dataset:
        line_dict = json.loads(line)
        bid = line_dict['business_id'].encode('utf-8')
        if bid not in business_id_set:
            continue
        uid = line_dict['user_id'].encode('utf-8')
        user_id_set.add(uid)
        reviews = line_dict['text'].encode('utf-8').replace('\n', ' ').replace('\r', '').replace(',', ' ')
        try:
            output[bid].append(reviews)
        except KeyError:
            output[bid] = [reviews]

    dataset.close()
    return output

data = data_constructor()
