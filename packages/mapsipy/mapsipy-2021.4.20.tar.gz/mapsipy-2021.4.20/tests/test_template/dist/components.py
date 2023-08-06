# -*- coding: utf-8 -*-
from mapsi import Mapsi, Component, DataStore

@Mapsi.register("helloworld-app")
class HelloWorld(Component):
    template = """
<div>
        <h1>{message}</h1>
    </div>
    """

    def __init__(self):
        super().__init__()

    def parameter():
        return {
            "message": str
        }
