from serpapi import GoogleSearch
import os

final_results = []

for query in ["guy outfit", "girl outfit"]:
    image_results = []

    params = {
        "engine": "google",               # specifies that we're using Google search engine
        "q": query,                    # search query
        "google_domain": "google.com",    # domain
        "tbm": "isch",                    # image results
        "num": 5,                         # num of images per page
        "ijn": 0,                         # first page of images
        "api_key": "085c9053b882e813230e799a46ea55cb5ac46ea682a8ce8d26e08104cd25275e"     # serpapi api key
    }

    search = GoogleSearch(params)       # data extraction

    images_is_present = True
    while images_is_present:
        results = search.get_dict()     # JSON -> Python dictionary\

        # checks for "Google hasn't returned any results for this query"
        if "error" not in results:
            for image in results["images_results"]:
                if image["original"] not in image_results:
                    image_results.append(image["original"])

            # update to the next page
            params["ijn"] += 1

            # new list of first five from both query searches
            final_results.append(image_results[:5]) # final_results returns lists within a list.
                                                    # Each sub list is the first 5 photos of each query search

            break
        
        else:
            images_is_present = False
            print(results["error"])


print(final_results)
print(len(final_results[0]))
print(len(final_results[1]))
