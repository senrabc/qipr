import pdb
class RelatedStore (object):

    def __init__(self):
        self.related = {}

    def add_related(self, key, value):
        if key not in self.related.keys():
            self.related[key] = []
        self.related[key].append(value)

    def clear(self):
        self.related = {}

    def associate_relateds(self, model):
        keys = self.related.keys()
        for key in keys:
            prop_name = key
            if key in dir(model):
                related_property = getattr(model, key)
                if related_property and getattr(related_property, "add"):
                    for item in self.related[key]:
                        related_property.add(item)
                else:
                    if len(self.related[key]) == 1:
                        item = self.related[key][0]
                        setattr(model, prop_name, item)


    def foreach(self, callback):
        for key in self.related.keys():
            for item in self.related[key]:
                callback(item)

