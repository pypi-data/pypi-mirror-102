from typing import List, Tuple, Optional

from pysciiart.widget import Widget, HBox, Size, Hints, VBox


class LayerModel():

    def __init__(self):
        self.__layers__ = [[]]

    def add(self, item: object) -> None:
        self.__layers__[0].append(item)

    def find_layer(self, item: object) -> Optional[int]:
        for ix, layer in enumerate(self.__layers__):
            if item in layer:
                return ix

        return None

    def shift(self, item: object) -> None:
        item_layer_index = self.find_layer(item)

        if item_layer_index == len(self.__layers__) - 1:
            self.__layers__.append([])

        self.__layers__[item_layer_index].remove(item)
        self.__layers__[item_layer_index + 1].append(item)

    def get_layers(self):
        return self.__layers__


class Graph(Widget):
    def __init__(self, widgets: List[Widget],
                 links: List[Tuple[Widget, Widget]]):
        layers = LayerModel()

        for w in widgets:
            layers.add(w)

        updated = True

        while updated:
            updated = False

            for link in links:
                ix1 = layers.find_layer(link[0])
                ix2 = layers.find_layer(link[1])

                if ix1 >= ix2:
                    layers.shift(link[1])
                    updated = True
                    break

        self._model = HBox([VBox(layer) for layer in layers.get_layers()])

    def preferred_size(self) -> Size:
        return self._model.preferred_size()

    def render(self, hints: Hints = None):
        return self._model.render(hints)
