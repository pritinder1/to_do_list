<tr>

    <td> {{ $post->id }}</td>
    <td>
        <a href = "/posts/{{ $post->id }}">
        {{ $post->body }}
        </a>
    </td>
    <td>{{ $post->completed }}</td>
    <td>{{ $post->created_at }}</td>
</tr>