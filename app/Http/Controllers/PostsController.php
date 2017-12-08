<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Post;

use Auth;

class PostsController extends Controller
{

    public function __construct(){

        $this->middleware('auth')->except(['index', 'show']);
    }

    public function index(){

       //$posts = Post::all();

        $posts = Post::all()->where('user_id', auth()->id()); 



       if(Auth::check()){


            if(request('desc')){
     

                    $temp = Post::orderBy('created_at', 'desc')->where('user_id', auth()->id());
                
            }else{


                $temp = Post::orderBy('created_at', 'asc')->where('user_id', auth()->id());


            }

            $posts = $temp->get();

        }


       


        return view('posts.index', compact('posts'));

    }

    public function show(Post $post)
    {
        //


        return view('posts.show', compact('post'));
    }

    public function create()
    {
        return view('posts.create');
    }

    public function store()
    {

        $this->validate(request(), [

            'body' => 'required',

        ]);


        auth()->user()->publish(

                new Post(request(['body', 'completed']))

            );


        return redirect('/');

    }

    public function edit(Post $post)
    {
        $post->body = request('body');
        $post->completed = request('completed');
        $post->save();
        return redirect('/');
    }

    public function destroy(Post $post)
    {
        //
        $post->delete();

        // redirect
        return redirect('/');
    }

}
