@extends('layout')

@section('content')

    @foreach($tasks as $task)
        <li>{{$task}}</li>
    @endforeach

@endsection