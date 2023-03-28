package zadanie10;

import java.util.stream.Stream;

/**
 * Napisz stream, który
 * 1) wypiszę użytkowników zarabiających więcej niż 5000
 *
 * 2) stworzy String, zawierający wszystkie adresy email oddzielone przecinkiem
 *
 * 3) wyświetli użytkownika o id 5, jeżeli nie ma takiego, wyświetli komunikat "Nie ma użytkownika o id 5"
 *
 * 4) wyświetli sumę zarobków programistów Javy, powyżej 25 roku życia
 */
public class Zadanie10 {
    public static void main(String[] args) {
        User user1 = new User(1L, "Ada", "Antczak", "a_antczak@email.com", 3456.5, 20, Job.JAVA_DEVELOPER);
        User user2 = new User(2L, "Beata", "Byk", "b_byk@email.com", 11223.5, 33, Job.SCALA_DEVELOPER);
        User user3 = new User(3L, "Czesław", "Cios", "c_cios@email.com", 6500.D, 33, Job.JAVA_DEVELOPER);
        User user4 = new User(4L, "Daria", "Chodkowska", "d_chodkowska@email.com", 2344.3, 40, Job.JAVA_DEVELOPER);
        User user5 = new User(5L, "Artur", "Boski", "a_boski@email.com", 8798.1, 21, Job.KOTLIN_DEVELOPER);
        User user6 = new User(6L, "Grzegorz", "Cyrych", "g_cytych@email.com", 12333D, 25, Job.GROOVY_DEVELOPER);
        User user7 = new User(7L, "Igor", "Drzewicki", "i_drzewicki@email.com", 12333D, 26, Job.JAVA_DEVELOPER);
        User user8 = new User(8L, "Lidia", "Figura", "l_figura@email.com", 1243D, 28, Job.SCALA_DEVELOPER);
        User user9 = new User(9L, "Norbert", "Gość", "n_gosc@email.com", 12322D, 45, Job.GROOVY_DEVELOPER);
        User user10 = new User(10L, "Urszula", "Grotkowska", "u_grotkowska@email.com", 11333D, 30, Job.SCALA_DEVELOPER);
        System.out.println("1) wypiszę użytkowników zarabiających więcej niż 5000");
        Stream<User> userStream1 = Stream.of(user1, user2, user3, user4, user5, user6, user7, user8, user9, user10);

        System.out.println("2) stworzy String, zawierający wszystkie adresy email oddzielone przecinkiem");
        Stream<User> userStream2 = Stream.of(user1, user2, user3, user4, user5, user6, user7, user8, user9, user10);

        System.out.println("3) wyświetli użytkownika o id 5, jeżeli nie ma takiego, wyświetli komunikat \"Nie ma użytkownika o id 5\"");
        Stream<User> userStream3 = Stream.of(user1, user2, user3, user4, user5, user6, user7, user8, user9, user10);

        System.out.println("4) wyświetli sumę zarobków programistów Javy, powyżej 25 roku życia");
        Stream<User> userStream4 = Stream.of(user1, user2, user3, user4, user5, user6, user7, user8, user9, user10);
    }
}
