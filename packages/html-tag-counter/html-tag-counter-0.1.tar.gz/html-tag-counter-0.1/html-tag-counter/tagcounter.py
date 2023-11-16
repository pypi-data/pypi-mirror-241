from database import select_from_db, save_results
import functions as fc
import logging


def main():
    logging.basicConfig(level=logging.INFO,                    # add logging
                        filename='tagcounter_log.log',
                        filemode='a',
                        format='%(asctime)s  - %(message)s')
    args = fc.parse_tagcounter_args()

    fc.parse_yaml_file()                                       # parse yaml-file

    if args.get is not None:                                   # tagcounter --get url
        url_get = fc.get_synonym(args.get)
        count_tags_get = fc.CountTags(url_get)
        tagcount_dict = count_tags_get.count_tags()            # returns a dictionary object
        pickled_tag_dict = fc.pickle_tag_dict(tagcount_dict)   # pickle dict to write to db
        full_url_get = fc.add_protocol_to_url(url_get)
        domain = fc.get_domain_site_by_url(full_url_get)       # extract 2nd level domain name
        save_results(full_url_get, domain, pickled_tag_dict)   # save results to db
        print(tagcount_dict)

    elif args.view is not None:                                # tagcounter --view url
        url_view = fc.get_synonym(args.view)
        full_url = fc.add_protocol_to_url(url_view)
        results = select_from_db(full_url)                     # connect to DB and execute select
        print(fc.unpickle_db_results(results))                 # unpickle results from DB

    elif args.view is None and args.get is None:               # tagcounter
        new_gui_window = fc.GuiWindow()
        new_gui_window.start()


if __name__ == "__main__":
    main()
