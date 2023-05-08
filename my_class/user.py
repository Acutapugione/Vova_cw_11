class User:
    def __init__(
        self,
        email,
        password,
    ):
        
        # 1 
        assert '@' in email #, 'Email must contains @ symbol'
        assert len(password) > 5, 'Password legth must be more than 5'
        
        # 2
        # if '@' not in email:
        #     raise Exception('Email must contains @ symbol')
        self.email = email
        self.password = password
        self.login = email.split('@')[0]


