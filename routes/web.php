<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
//php artisan make:model Task -m
Route::post('/posts', 'PostsController@store');
Route::get('/tasks','TasksController@index');
Route::get('/posts/create', 'PostsController@create');
//php artisan make:controller TasksController -r  <-makes resourcefull controller
Route::patch('/posts/{post}/edit', 'PostsController@edit');
Route::delete('/posts/{post}/delete', 'PostsController@destroy');
Route::get('/posts/{post}', 'PostsController@show');

Route::get('/', 'PostsController@index')->name('home');

Route::post('/posts/{post}/comments', 'CommentsController@store');

Route::get('about', function(){

    return 'test';
});


Route::get('/register', 'RegistrationController@create');
Route::post('/register', 'RegistrationController@store');

Route::get('/login', 'SessionsController@create')->name('login');
Route::post('/login', 'SessionsController@store');
Route::get('/logout', 'SessionsController@destroy');


