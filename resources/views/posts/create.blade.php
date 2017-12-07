@extends('layout')

@section('content')

    <form action="/posts" method="post" class="col-sm-8" style="padding: 100px 15px;">

        <div class="form-group">
            {{ csrf_field() }}
            <label for="taskTitle">Task Title</label>
            <input type="text" class="form-control" id="taskTitle" name="body">
        </div>
        <div class="form-group">
            <label for="taskStatus">Task Status</label>
            <select class="form-control" id="taskStatus" name="completed" selected="0">
                <option value="0">Incomplete</option>
                <option value="1">Complete</option>
            </select>
        </div>

        <div class="form-group">

         <button type="submit" class="btn btn-primary">Create</button>

        </div>



        @if (count($errors))

            <div class="form-group">
                <div class="alert alert-danger">
                    <ul>
                        @foreach($errors->all() as $error)

                            <li>{{ $error }}</li>

                        @endforeach
                    </ul>
                </div>
            </div>

        @endif

    </form>

@endsection