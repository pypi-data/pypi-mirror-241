import enum


class ClientAssertionType(str, enum.Enum):
    jwt     = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
    saml2   = 'urn:ietf:params:oauth:client-assertion-type:saml2-bearer'