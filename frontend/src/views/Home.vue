<template>
  <div class="carousel">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="3000">
          <div class="carousel-image"><img src="./static/carousel/carousel1.jpg" class="d-block w-100" alt="..."></div>
          <div class="carousel-caption d-none d-md-block">
            <div class="text-black">
              <h5>Universal Library</h5>
              <p>One stop library for every bibiliophiles</p>
            </div>
          </div>
        </div>
        <div class="carousel-item"  data-bs-interval="3000">
          <div class="carousel-image"><img src="./static/carousel/carousel2.jpg" class="d-block w-100" alt="..."></div>
          <div class="carousel-caption d-none d-md-block">
            <div class="text-black">
              <h5>Guaranteed Price</h5>
              <p>Lowest ever price available on the internet</p>
            </div>
          </div>
        </div>
        <div class="carousel-item"  data-bs-interval="3000">
          <div class="carousel-image"><img src="./static/carousel/carousel3.jpg" class="d-block w-100" alt="..."></div>
          <div class="carousel-caption d-none d-md-block">
            <div class="text-black">
              <h5>Easy Borrowing</h5>
              <p>Quick access on book borrow requests</p>
            </div>
          </div>
        </div>
      </div>
      <div class="left-button">
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
      </div>
      <div class="right-button">
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>
  <hr>

  <div class="showcase-books">
    {% for genre in genres %}
      <div class="genres">
        <h2>{{genre.name}}</h2>
        <hr>
           <div class="flex-container">
             <div class="arrow arrow-left" onclick="scrollList('left')"><i class="fa-solid fa-arrow-left"></i></div>
             <div class="scroll-container">
                   {% for book in genre.books %}
                    {% if (parameter=="book" and query.lower() in book.title.lower()) or (parameter == "price" and query >= book.price) or (parameter=="genre") or (not parameter) %}
                        <div class="card" >
                          <a href="{{ url_for("book", book_id=book.id) }}"><img src="{{book.image}}" class="card-img-top" height="250px" width="500px" alt="..."></a>
                          <div class="card-body">
                            <a href="{{ url_for("book", book_id=book.id) }}">
                              <h6 class="card-title"><strong>{{ book.title }}</strong></h6>
                            </a>
                            <p class="card-text"><span class="text-muted">Price :</span>&nbsp;&nbsp;<span style="color:red;">&#8377;{{ book.price }}</span></p>
                            <div class="card-buttons">
                              {% if book.quantity > 0 %}
                                <a href="{{ url_for("add_to_cart", book_id=book.id) }}" method="post" class="btn btn-success btn-sm">Add to cart</a>
                                <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#staticBackdrop{{book.id}}">Borrow</button>
             
                                <!-- Modal -->
                                <div class="modal fade" id="staticBackdrop{{ book.id }}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered">
                                        <div class="modal-content">
                                            <div class="modal-header bg-secondary bg-gradient text-white">
                                                <h5 class="modal-title" id="staticBackdropLabel">Select Borrowing Duration</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <div class="modal-body">
                                                <p class="lead">Choose the number of days you want to borrow the book "{{ book.title }}".</p>
                                                <form action="{{ url_for('add_to_request', book_id=book.id) }}" method="post">
                                                    <div class="mb-3">
                                                        <label for="daysRequested" class="form-label">Number of Days:</label>
                                                        <input type="number" class="form-control" id="daysRequested" name="days_requested" value="14" min="7" max="60">
                                                    </div>
                                                    <div class="text-end">
                                                        <button type="submit" class="btn btn-primary">Request</button>
                                                    </div>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>

             
                              {% else %}
                                <button class="btn btn-outline-danger btn-sm" disabled><i class="fa-solid fa-x"></i>  Out of stock</button>
                              {% endif %}
                            </div>
                          </div>
                        </div>
                    {% endif %}
                   {% endfor %}
             </div>
             <div class="arrow arrow-right" onclick="scrollList('right')"><i class="fa-solid fa-arrow-right"></i></div>
           </div>
            </div>
               {% endfor %}
             </div>
         </div>
{% endblock %}
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>

  .carousel-image {
    width: 100%;
    height: 300px;
  }

  .carousel {
    margin: 20px 10px 20px 10px;
  }

  .showcase-books {
    display: flex;
    flex-direction: column;
    margin: 20px;
  }

  .flex-container {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .genres {
    margin: 20px 0 20px 0;
  }

  .scroll-container {
    display: flex;
    overflow-x: auto;
    flex-wrap: nowrap;
    width: 95%;
    margin: 0 auto;
  }

  .scroll-container::-webkit-scrollbar {
    display: none; 
  }

  .card {
    flex: 0 0 auto;
    margin: 0 10px;
    width: 13rem;
    height: 25rem;
  }

  .card-buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  .arrow {
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    font-size: 20px;
    color: #333;
    margin-left: 5px;
    margin-right: 5px;
  }

  .arrow-left {
    right: 5px;
  }

  .arrow-right {
    left: 5px;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
    color: blue;
  }

</style>