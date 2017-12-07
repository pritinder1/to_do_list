@extends('layout')

@section('content')

    <div class = "col-sm-8" style="padding: 100px 40px;">




        <form action="/posts/{{ $post->id }}/edit" method="post" class="col-sm-8"">

        <div class="form-group">
            {{ csrf_field() }}
            {{ method_field('PATCH') }}
            <label for="postTitle">Task Title</label>
            <input type="text" class="form-control" id="postTitle" name="body" value="{{ $post->body }}">
        </div>

        <div class="form-group">
            <label for="postStatus">Task Status</label>
                @if ($post->completed === 1)
                    <select class="form-control" id="postStatus" name="completed" value="{{ $post->completed }}">

                            <option value="1" selected>Complete</option>
                            <option value="0">Incomplete</option>
                    </select>
                @else

                    <select class="form-control" id="postStatus" name="completed" value="{{ $post->completed }}">

                        <option value="1" >Complete</option>
                        <option value="0" selected>Incomplete</option>

                    </select>

                @endif


        </div>



        <button style="margin-bottom: 10px;" type="submit" class="btn btn-primary">Save</button>



        </form>


        <p>


        <form action="/posts/{{ $post->id }}/delete" method="post" class="col-sm-8">
            {{ csrf_field() }}
            {{ method_field('DELETE') }}
            <button type="submit" class="btn btn-primary">Delete</button>

        </form>
        Created by: {{ $post->user->name }} <br>
        Created on: {{date("F d, Y h:i:s", strtotime( $post->created_at ))}} <br>
        Updated on: {{ $post->updated_at }}</br>
        </p>



    

<div class = "comments" style="padding-top: 300px">

     <h1>Comments</h1>

     <hr>

    
        
        <ul class="list-group">
            
        @foreach ($post->comments as $comment)

            <li class="list-group-item">

                <strong>
                    
                {{ $comment->created_at->diffForHumans() }}: &nbsp;

                </strong>


                {{ $comment->body }}

            </li>

             @endforeach
        </ul>

   

    </div>

    <hr>
    
    <div class="card">
        

    <div class="card-block">
        
            <form method="POST" action="/posts/{{ $post->id }}/comments">

            {{ csrf_field() }}
                
            <div class="form-group">
                
                <textarea name="body" placeholder="Leave a Comment Below !!" class="form-control"></textarea>

            </div>

            <div class="form-group">

                <button type="submit" class="btn btn-primary">Add Comment</button>

            </div>

            </form>

    </div>

    </div>


@endsection

