import os
from typing import Optional, Union, Type, List, TYPE_CHECKING

from cose import utils
from cose.exceptions import CoseInvalidKey, CoseIllegalKeyType, CoseIllegalKeyOps
from cose.keys.cosekey import CoseKey
from cose.keys.keyops import MacCreateOp, MacVerifyOp, EncryptOp, DecryptOp, UnwrapOp, WrapOp
from cose.keys.keyparam import KpKty, SymmetricKeyParam, SymKpK, KeyParam
from cose.keys.keytype import KtySymmetric

if TYPE_CHECKING:
    from cose.keys.keyops import KEYOPS


@CoseKey.record_kty(KtySymmetric)
class SymmetricKey(CoseKey):

    @classmethod
    def from_dict(cls, cose_key: dict) -> 'SymmetricKey':
        """
        Returns an initialized COSE Key object of type SymmetricKey.

        :param cose_key: Dict containing COSE Key parameters and their values.

        :return: an initialized COSE SymmetricKey object
        """

        if SymKpK in cose_key:
            key_bytes = cose_key[SymKpK]
        elif SymKpK.identifier in cose_key:
            key_bytes = cose_key[SymKpK.identifier]
        elif SymKpK.fullname in cose_key:
            key_bytes = cose_key[SymKpK.fullname]
        else:
            raise CoseInvalidKey("COSE Symmetric Key must have an SymKpK attribute")

        return cls(k=key_bytes, optional_params=cose_key, allow_unknown_key_attrs=True)

    @staticmethod
    def _key_transform(key: Union[Type['SymmetricKeyParam'], Type['KeyParam'], str, int],
                       allow_unknown_attrs: bool = False):
        return SymmetricKeyParam.from_id(key, allow_unknown_attrs)

    def __init__(self, k: bytes, optional_params: Optional[dict] = None, allow_unknown_key_attrs: bool = True):
        transformed_dict = {}

        if len(k) not in [16, 24, 32]:
            raise CoseInvalidKey("Key length should be either 16, 24, or 32 bytes")

        new_dict = dict({KpKty: KtySymmetric, SymKpK: k})

        if optional_params is not None:
            new_dict.update(optional_params)

        for _key_attribute, _value in new_dict.items():
            try:
                # translate the key_attribute
                kp = SymmetricKeyParam.from_id(_key_attribute, allow_unknown_key_attrs)

                # parse the value of the key attribute if possible
                if hasattr(kp, 'value_parser') and hasattr(kp.value_parser, '__call__'):
                    _value = kp.value_parser(_value)

                # store in new dict
                transformed_dict[kp] = _value
            except ValueError:
                transformed_dict[_key_attribute] = _value

        # final check if key type is correct
        if transformed_dict.get(KpKty) != KtySymmetric:
            raise CoseIllegalKeyType(f"Illegal key type in Symmetric COSE Key: {transformed_dict.get(KpKty)}")

        super(SymmetricKey, self).__init__(transformed_dict)

    def __delitem__(self, key):
        if self._key_transform(key) != KpKty and self._key_transform(key) != SymKpK:
            super().__delitem__(key)
        else:
            raise CoseInvalidKey(f"Deleting {key} attribute would lead to an invalide COSE Symmetric Key")

    @property
    def k(self) -> bytes:
        """ Returns the mandatory :class:`~cose.keys.keyparam.SymKpK` attribute of the COSE Symmetric Key object. """
        if SymKpK in self.store:
            return self.store[SymKpK]
        else:
            raise CoseInvalidKey("Symmetric COSE key must have the SymKpK attribute")

    @k.setter
    def k(self, k: bytes):

        if type(k) is not bytes:
            raise ValueError("symmetric key must be of type 'bytes'")
        self.store[SymKpK] = k

    @property
    def key_ops(self) -> List[Type['KEYOPS']]:
        """ Returns the value of the :class:`~cose.keys.keyparam.KpKeyOps` key parameter """

        return CoseKey.key_ops.fget(self)

    @key_ops.setter
    def key_ops(self, new_key_ops: List[Type['KEYOPS']]) -> None:
        supported = {MacCreateOp, MacVerifyOp, EncryptOp, DecryptOp, UnwrapOp, WrapOp}
        for ops in new_key_ops:
            if not self._supported_by_key_type(ops, supported):
                raise CoseIllegalKeyOps(f"Invalid COSE key operation {ops} for key type {SymmetricKey.__name__}")
            else:
                CoseKey.key_ops.fset(self, new_key_ops)

    @staticmethod
    def generate_key(key_len: int, optional_params: dict = None) -> 'SymmetricKey':
        """
        Generate a random Symmetric COSE key object.

        :param key_len: Symmetric key length in bytes, must be of size 16, 24 or 32.
        :param optional_params: Optional key attributes for the :class:`~cose.keys.symmetric.SymmetricKey` object, \
        e.g., :class:`~cose.keys.keyparam.KpAlg` or  :class:`~cose.keys.keyparam.KpKid`.

        :raises ValueError: For invalid key lengths.

        :returns: A COSE_key of type SymmetricKey.
        """

        if key_len not in [16, 24, 32]:
            raise ValueError("key_len must be of size 16, 24 or 32")

        return SymmetricKey(k=os.urandom(key_len), optional_params=optional_params)

    def __repr__(self):
        _key = self._key_repr()

        if 'SymKpK' in _key and len(_key['SymKpK']) > 0:
            _key['SymKpK'] = utils.truncate(_key['SymKpK'])

        hdr = f'<COSE_Key(Symmetric): {_key}>'

        return hdr


SK = SymmetricKey

if __name__ == '__main__':
    print(SymmetricKeyParam.get_registered_classes())
