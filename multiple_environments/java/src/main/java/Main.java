import locker.LockerClient;
import locker.exception.LockerError;
import locker.model.Environment;
import locker.model.Secret;
import locker.param.environment.EnvironmentCreateParams;
import locker.param.secret.SecretCreateParams;

public class Main {
    public static void main(String[] args) {
        LockerClient client = new LockerClient();
        EnvironmentCreateParams stagingEnvParams = EnvironmentCreateParams
                .builder()
                .setName("staging")
                .setExternalUrl("staging.com")
                .setDescription("Staging environment")
                .build();
        EnvironmentCreateParams productEnvParams = EnvironmentCreateParams
                .builder()
                .setName("product")
                .setExternalUrl("product.com")
                .setDescription("Product environment")
                .build();

        try {
            // Create 2 environments: staging and product
            Environment stagingEnv = client.environments().create(stagingEnvParams, Environment.class);
            Environment productEnv = client.environments().create(productEnvParams, Environment.class);

            // Create secret for each environment
            SecretCreateParams secretStagingParam = SecretCreateParams
                    .builder()
                    .setKey("host")
                    .setValue("staging_host")
                    .setDescription("Host for staging environment")
                    .setEnvironmentName("staging")
                    .build();
            SecretCreateParams secretProductParam = SecretCreateParams
                    .builder()
                    .setKey("host")
                    .setValue("product_host")
                    .setDescription("Host for product environment")
                    .setEnvironmentName("product")
                    .build();
            Secret hostStaging = client.secrets().create(secretStagingParam, Secret.class);
            Secret hostProduct = client.secrets().create(secretProductParam, Secret.class);

            System.out.println(stagingEnv);
            System.out.println(productEnv);
            System.out.println(hostStaging);
            System.out.println(hostProduct);

            // Retrieve secret
            String hostStagingValue = client.secrets().retrieve("host", String.class, "staging");
            String hostProductValue = client.secrets().retrieve("host", String.class, "product");
            System.out.println("Host value of staging environment: " + hostStagingValue);
            System.out.println("Host value of product environment: " + hostProductValue);

        } catch (LockerError e) {
            e.printStackTrace();
        }
    }
}