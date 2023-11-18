from verysimpletransformers import to_vst
from verysimpletransformers.types import DummyModel


def main():
    def get_cls():
        class MyClass(DummyModel):
            ...

        return MyClass

    model = get_cls()()

    to_vst(model, 'test.vst')


if __name__ == '__main__':
    main()
