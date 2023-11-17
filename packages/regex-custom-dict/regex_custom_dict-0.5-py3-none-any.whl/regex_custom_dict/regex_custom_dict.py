import re
class RegexCustomDict(dict):
    
    def flatten_dict(self):
        if all(ele.startswith("$$") for ele in super().keys()):
            dict_values=list(super().values())
            if len(dict_values)==1:
                return dict_values[0]
            return dict_values
    
    def apply_regex_on_key(self,key):
        list_all_keys=super().keys()
        if isinstance(key,str):
            re_pattern=re.compile(r'{}'.format(key))
            list_all_matched_keys=[matched_key for matched_key in list_all_keys if re_pattern.match(matched_key)]
            value_out_dict=RegexCustomDict()
            for index,matched_key in enumerate(list_all_matched_keys):
                value=super().__getitem__(matched_key)
                if isinstance(value, dict):
                    value=RegexCustomDict(**value)
                value_out_dict.update({"$$re_match_{}$$".format(index):value})
            return value_out_dict      
        else:
            return super().__getitem__(key)
            
    def __getitem__(self,key):
        list_all_keys=super().keys()
        if any(ele.startswith("$$") for ele in list_all_keys):
            values=self.flatten_dict()
            if isinstance(values,list) is False:
                values=[values]
            combined_dict=RegexCustomDict()
            index=0
            for value in values:
                if isinstance(value, RegexCustomDict):
                    matched_values=value.apply_regex_on_key(key).flatten_dict()
                    if isinstance(matched_values,list) is False:
                        matched_values=[matched_values]
                    for matched_value in matched_values:
                        combined_dict.update({"$$re_match_{}$$".format(index):matched_value})
                        index += 1
            return combined_dict
        else:
            return self.apply_regex_on_key(key)


