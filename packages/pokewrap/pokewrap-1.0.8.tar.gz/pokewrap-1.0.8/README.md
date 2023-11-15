# Pokewrap v1.0.8

A wrapper library for the PokeAPI making it easier to build into other python scripts through a quick import. This library is a personal project to done to learn more about package creation and publishing.

Pokewrap is not regularly updated, and works with current versions of Python.

Please feel free to use it in any of your projects, deconstruct it, and learn from it. If you find any bugs, you can [submit an issue](https://github.com/jasongarvin/pokewrap/issues) and I'll work on resolving it ASAP.

## How it works

Pokewrap relies on objects to handle communicating with the API and parse data into meaningful chunks. This ensures a smooth experience working with the returned json, since the objects that wrap it help provide more meaningful access to the data.

You can use Pokewrap to connect with the API endpoint and request specific pokemon, or use the generic controller to request berries and other resources. The goal of Pokewrap is to abstract away formatting the API call and parse the returned json for you so you don't have to sweat the details.

You can also use it Pokewrap to see which endpoints are available if you're unsure where to start or need to generate a way to pull from several endpoints.

## Getting Started

You can either import the library using pip, pulling from the PyPI database, or by downloading this repository. You can also clone/fork this repository to edit it in your own workspace.

---

To use Pokewrap, first import it into your script or service:

```python
import pokewrap
```

Then you can start making requests using the ApiController class or choose a resource-specific wrapper (currently only available for Pokemon).

Set up the class by specifying as str the type of resource and the specific resource, or as int the Pokemon ID number.

For example, to see the Pokemon "Gengar" and its information, set:

```python
ApiController("pokemon", "gengar")
```

Or, using the ID:

```python
ApiController("pokemon", 94)
```

If you'd prefer to use the wrapper class, Pokemon, you can simply request information for a Pokemon in the following way:

```python
Pokemon("gengar")   # Using the name
```

```python
Pokemon(94)         # Using the ID
```

You can also use ApiResourceList to get a dictionary response of all viable resources within a supertype (or access the global variable RESOURCE_ENDPOINTS).

For example, to see every Pokemon available through the endpoint:

```python
ApiResourceList("pokemon")
```

Or use limit/offset values to improve the specificity of your query, overriding the default limits set by PokeAPI:

```python
ApiResourceList("pokemon", limit=100, offset=2)
```

Note that the default limit is 20 for resource requests. For larger sets of data, please specify the limit in the function call.

For a conprehensive list of all available resource types, check the static RESOURCE_TYPE variable or the dynamically-generated RESOURCE_ENDPOINTS variable.

## Requesting changes

If you run into an issue or find a bug, please [submit an issue](https://github.com/jasongarvin/pokewrap/issues) and I'll get the fix rolled out as soon as I can.

Since this is intended as a learning project, I don't have immediate plans to continue updating Pokewrap. That said, anyone is more than welcome to submit pull requests and I will approve/add code as applicable. I'm also constantly keeping an eye on the library to at least ensure it continues working.
