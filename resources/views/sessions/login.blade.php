@extends ('layout')



@section ('content')


	<div class="col-md-8">
		
	<h1>Sign In</h1>

<form method="POST" action="/login">
		
		{{ csrf_field() }}


		<div class = "form-group" >
			
			<label for="email">Email:</label>

			<input type="email" class="form-control" name="email" id="email" required>

		</div>

		
		<div class = "form-group" >
			
			<label for="password">Password</label>

			<input type="password" class="form-control" name="password" id="password" required>

		</div>

		
		<div class = "form-group" >
			
			<button type="submit" class="btn btn-primary">Sign In</button>

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

	</div>




@endsection