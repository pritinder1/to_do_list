@extends ('layout')



@section('content')


    <div class="starter-template">
        <h1>Create Your Daily To-Do List</h1>
        <p class="lead">This site will help you orgainze all your daily tasks<br> Ensuring that all your work gets complete</p>
    </div>


    <div class="container">
        <h2>To-Do List</h2>
        <p>Status: 0 = Incomplete, 1 = Complete</p>
        <table class="table table-bordered">

            <tr>

                <th>ID#</th>
                <th>To-Do Task</th>
                <th>Status</th>
                <th>Create On</th>

            </tr>

          

            @if ($posts->isEmpty())

                <a href="https://prince.dev/posts/create">Create A Task</a>


            @else

                @foreach($posts as $post)

                    @include ('posts.summary')

                @endforeach


            @endif



        </table>

          <a href="?asc=true"><button type="submit" class="btn btn-primary">Ascending</button></a>

          <a href="?desc=true"><button type="submit" class="btn btn-primary">Descending</button></a>

            


    </div>

@endsection