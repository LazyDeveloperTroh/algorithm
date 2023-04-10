# 프로젝트 환경

	springboot 3.0.5, java 17, gradle 7.6.1


# 프로젝트 구조

	클라이언트와 서버 패키지로 구성되어 있고 클라이언트(OrderClient)는 API(ProductApi, OrderApi)를 통해 서버와 통신할 수 있습니다.
	콘솔 기반의 프로그램이기 때문에 서버 측 로그는 출력하지 않도록 하였으며 중요 객체인 경우 테스트를 작성하여 안정적인 개발이 가능하도록 하였습니다.

	주문 프로그램은 ProductApi를 이용하여 상품정보(ProductDto)를 출력하며 사용자의 주문정보(OrderRequestItem)를 입력받아 장바구니(Cart)객체에 담고
	사용자가 결제를 요청하면 OrderApi를 이용하여 서버에 요청합니다. 주문이 성공적으로 처리되는 경우 주문 결과(OrderResult)를 출력하며 재고가 부족하거나
	그 외 오류가 발생하는 경우 오류 메세지를 출력합니다.

# 핵심 요구사항에 대한 구현 방향
- 한 번에 여러개의 상품을 같이 주문할 수 있어야 한다.
  > 장바구니(Cart)객체를 이용하였고 결제 요청이 있기 전까지 장바구니에 주문정보(OrderRequestItem)를 추가하고 
      고객이 결제를 요청했을 때 Cart에 담긴 주문정보 전체를 서버에 전송하는 방식으로 구현했습니다.
    (단, 동일한 상품을 추가하는 경우 수량을 합하여 한 종류의 상품만 저장)
      
- 결제 시 재고가 부족할 경우 SoldOutException이 발생
  > 결제를 처리할 때 재고 체크, 재고 감소로직이 있기 때문에 멀티쓰레드 환경에서 Thread-safe를 보장하기 위해 synchronized를 사용하였습니다.
    (SoldOutException 관련 테스트 코드는 kr.co._29cm.homework.server.service.impl.OrderServiceImplTest에 작성하였습니다)
    

- 주문 금액이 5만원 미만인 경우 배송비 2,500원이 추가
  > 현재는 주문 금액에 따른 배송비 여부만 판단하고 있지만 이후에는 쿠폰 적용, 10% 할인 등 지불 금액에 대한 다양한 변화가 있을 수 있기 떄문에
      Strategy 패턴을 사용하여 지불 금액과 배송비에 대한 로직을 분리하였습니다.
    (주문결과(OrderResult)객체를 생성할 때 가격전략(DefaultOrderPriceStrategy)을 전달하여 지불금액과 배송비를 계산)
    

- 상품 데이터(csv) 관리
   > 상품 데이터는 상품정보(Product)와 재고정보(Stock)로 분리하였고 각각 메모리에서 관리할 수 있도록 했습니다.(ProductMemoryRepository, StockMemoryRepository)
    현재는 메모리에서 데이터를 저장하고 있지만 이후에는 저장소가 변경되는 것을 대비하여 서비스 클래스에서는 인터페이스에 의존하도록 구현했습니다.




