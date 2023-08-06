'''
:usage:
    specimen = {
        "name": "Ranadebilla",
        "speaks": {
            'phrases': ['kavali', 'hello']
        },
        "favourite-phrase": 'hello'
    }

    hello_to_hi = lambda greet: 'hello' if greet=='hi' else greet

    mutate(specimen, hello_to_hi)

    specimen mutated to -> {
                        "name": "Ranadebilla",
                        "speaks": {
                            'phrases': ['kavali', 'hi']
                        },
                        "favourite-phrase": 'hi'
                    }
'''
import typing

supported_entry_types = dict, list, tuple, set


def enhanced_enumertor(enumerable):
    if isinstance(enumerable, dict):
        return enumerable.items()
    return enumerate(enumerable)


def _mutate(specimen, mutating_function):
    # for key in specimen:
    for key, inner_specimen in enhanced_enumertor(specimen):
        # Call recursively if the specimen is a dict
        if isinstance(inner_specimen, dict):
            _mutate(inner_specimen, mutating_function)

        # Recurse iteratively if its an iterable, ignore str type
        elif isinstance(inner_specimen, typing.Iterable) and not isinstance(
                inner_specimen, str):
            _mutate(inner_specimen, mutating_function)

        # Mutate the specimen
        else:
            if not isinstance(specimen, typing.Hashable):
                # check for set
                if isinstance(specimen, set):
                    specimen.remove(inner_specimen)
                    specimen.add(mutating_function(inner_specimen))
                else:
                    specimen[key] = mutating_function(inner_specimen)
            else:
                # TODO: Add warnings
                print('skipping immutables')


def mutate(specimen, mutating_function):
    '''
    Mutates the values of a dictionary using the provided mutating_function
    Ideal for mutating the JSON values.

    :params:
    specimen:
        type: dict
        description: The dictionary whose values get mutated.
    mutating_function:
        type: function
        description: Use this function to mutate each value in a specimen.

    :warnings:
    mutating_function: function must return a value unless you want None as the
    mutated value.

    '''
    if not isinstance(specimen, supported_entry_types):
        raise TypeError(
            'Invalid specimen type: %s, specimen must be any of the (%s, %s, \
             %s, %s)' % (type(specimen), *supported_entry_types))
    _mutate(specimen, mutating_function)


if __name__ == '__main__':

    def hi_to_hello(greet):
        return 'hello' if greet == 'hi' else greet

    # TODO: Add testing env, pytest
    d = {
            'greet': 'hi',
            'list_of_greetings': [
                'hello',
                'good morning',
                'hi',
            ],
            'container_of_greetings': [
                (
                    'hi',
                     {
                        'greet':
                        'hi',
                        'tuple_of_greetings': ('hi', 'good evening')
                     },
                     (
                           'greet',
                           'hi'
                     )
                ),
                (
                    {
                        'greet': 'hi'
                    },
                )
            ]
    } # yapf: disable
    mutate(d, hi_to_hello)
    print(d)
