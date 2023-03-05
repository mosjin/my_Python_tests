from functools import wraps, update_wrapper


class logit( object ):
    _logfile = 'out.log'

    def __init__( self, func ):
        self.func = func
        update_wrapper( self, func )
        print( f"{self._logfile}, {logit.__init__.__qualname__}, {self.func}" )

    def __call__( self, *args, **kwargs ):
        print( f"log count: {type( args )}, {args}" )
        print( f"log kwargs: {type( kwargs )}, {kwargs}" )
        if 'log_str' in kwargs:
            print( f"log_str: {kwargs[ 'log_str' ]}" )
        if 'counter' in kwargs:
            counter = kwargs[ 'counter' ]
            print( f"counter: {counter[ 0 ]}, {counter[ 1 ]}" )
        self.notify()

        return self.func( self, *args )

    def notify( self ):
        print( f"notify" )


class email_log( logit ):
    def __init__( self, func, email = 'afrl@163.com' ):  # , *args, **kwargs ):
        self.func = func
        self.email = email
        update_wrapper( self, func )
        print( f"email: {self.email}" )
        super( email_log, self ).__init__( func )

    def notify( self ):
        print( f"********email: {self.email}" )


class ABC():
    def __init__( self ):
        pass

    @email_log
    def log( self, p1, p2 ):
        print( f"log()...{p1}, {p2}" )

    @logit
    def log_it( self, name, count ):
        print( f"{ABC.log_it.__qualname__}, name: {name}, count: {count}" )


# @logit
@email_log
def log_count( tip, number = 1 ):
    print( f"##########{log_count},log_count: tip: {tip}; nuber: {number}" )
    pass


result = log_count( "hi, lan", log_str = "haha", counter = ("COUNT_CNT", 3) )

print( "\n" )
abc = ABC()
abc.log( 3, "p2", log_str = "hi", counter = ("CNT", 23) )

abc.log_it( "zs", 23, counter = ("LOG_IT_CNT", 3) )
print( "___")
abc.log_it( "zs", 23, log_str= "zs23" )
