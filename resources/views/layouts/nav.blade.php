<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Task Manager</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="https://prince.dev/">Home</a></li>
                <li><a href="https://prince.dev/posts/create">Create</a></li>
            </ul> 

            <ul style = "float:right;" class="nav navbar-nav">
                <li style="padding-right: 10px;"> @if (Auth::check())

                <a class="nav-link ml-auto" href="#">{{Auth::user()->name }}</a>
                <li><a href="https://prince.dev/logout">Logout</a></li>

                    @else 

                <li><a href="https://prince.dev/login">Login</a></li>
                <li><a href="https://prince.dev/register">Register</a></li>

                 @endif </li>
                
            </ul>
        </div><!--/.nav-collapse -->
    </div>
</nav>